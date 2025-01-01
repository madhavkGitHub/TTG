from flask import Flask, render_template, request, json, jsonify
import MakeExpression
import sympy
import GetValue
import BackToSympy
import Validator
import matplotlib.pyplot as plt
import random
import time
import os
import shutil

valid = 0
invalid = 0
avg_valid_time = 0
avg_invalid_time = 0

expr = None
sign = ""
symbol_set = set()
start = 0
index = 0
loc = ""

all_equations = []
loaded = False

filt = False

run_once = False

custom = ""

def clear():
    folder = 'static\\images\\storage'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def save(satisfies):
    global run_once
    if not loaded:
        run_once = False
        if satisfies == False:
            with open("results\\expressions.txt", "a") as f:
                f.write("invalid: " + str(expr) + " " + sign + "\n")
            with open("results\\invalid_times.txt", "a") as f:
                f.write(str(round(time.time() - start, 2)) + "\n")
        else:
            l = []
            for k in satisfies.keys():
                if satisfies[k]:
                    l.append(k)
            with open("results\\expressions.txt", "a") as f:
                f.write("valid: " + str(expr) + " " + sign + " " + str(l) + "\n")
            with open("results\\valid_times.txt", "a") as f:
                f.write(str(round(time.time() - start, 2)) + "\n")

def statistics():
    global valid, invalid, avg_valid_time, avg_invalid_time
    equations = []
    invalid_times = []
    valid_times = []
    f = (open("results\\expressions.txt", "r")).readlines()
    i = (open("results\\invalid_times.txt", "r")).readlines()
    v = (open("results\\valid_times.txt", "r")).readlines()
    for line in f:
        equations.append(line.strip())
        if line.count("invalid") == 1:
            invalid_times.append(float((i[len(invalid_times)]).strip()))
        else:
            valid_times.append(float((v[len(valid_times)]).strip()))
    valid = len(valid_times)
    invalid = len(invalid_times)
    if valid > 0:
        avg_valid_time = round(sum(valid_times)/valid,2)
    if invalid > 0: 
        avg_invalid_time = round(sum(invalid_times)/invalid,2)


def make_img(latex_expression, loc):
    fig = plt.figure(figsize=(4, 1))  # Dimensions of figsize are in inches
    text = fig.text(
        x=0.5,  # x-coordinate to place the text
        y=0.5,  # y-coordinate to place the text
        s=latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=16,
    )
    plt.savefig(loc)


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/Find')
def Find():
    global expr, symbol_set, index, loc, sign, loaded
    statistics()
    folder = "static\\images\\equations"
    count = len(os.listdir(folder))
    while True:
        expr, latex, symbol_set = MakeExpression.generate_expression()
        if expr == None:
            continue
        inequality = ["= 1", "> 1", "< 1", ">= 1", "<= 1"]
        sign_to_latex = {"= 1" : "= 1", "> 1" : "> 1", "< 1": "< 1", ">= 1": "\\geq 1", "<= 1" : "\\leq 1"}
        index = random.randint(0, 4)
        latex += " " + sign_to_latex[inequality[index]]
        sign = inequality[index]
        loc = folder + "\\equation" + str(count + 1) + ".png"
        make_img("$" + latex + "$", loc)
        loaded = False
        return render_template("Find.html", src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)
 
@app.route('/Enter')
def Enter():
    return render_template("Enter.html")

@app.route('/Custom')
def Custom():
    global expr, symbol_set, index, loc, sign, loaded, custom
    data = BackToSympy.parseNewTheorem(custom)
    statistics()
    inequality = ["=", ">", "<", ">=", "<="]
    sign_to_latex = {"=" : "= 1", ">" : "> 1", "<": "< 1", ">=": "\\geq 1", "<=" : "\\leq 1"}
    folder = "static\\images\\equations"
    count = len(os.listdir(folder))
    expr, latex, symbol_set = data[0], sympy.latex(data[0]), data[1]
    index = data[2]
    latex += " " + sign_to_latex[inequality[index]]
    loc = folder + "\\equation" + str(count + 1) + ".png"
    make_img("$" + latex + "$", loc)
    loaded = False
    return render_template("Find.html", src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)

@app.route('/Validate')
def Validate():
    global start
    start = time.time()
    print(symbol_set, expr, index)
    satisfies = Validator.valid(symbol_set, expr, index)
    save(satisfies)
    statistics()
    return render_template("Validate.html", satisfies=satisfies, src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)

@app.route('/Load/<number>')
def Load(number):
    global symbol_set, expr, index, loc, loaded
    data = all_equations[int(number)]
    print(data)
    symbol_set = data[4]
    expr = data[2]
    index = data[3]
    satisfies = True
    if data[0] == "invalid":
        satisfies = False
    loc = "..\\static\\images\\storage\\image" + number + ".png"
    statistics()
    loaded = True
    return render_template("Validate.html", satisfies=satisfies, src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)

@app.route('/FindMany')
def FindMany():
    global expr, symbol_set, index, loc, sign
    statistics()
    folder = "static\\images\\equations"
    count = len(os.listdir(folder))
    while True:
        expr, latex, symbol_set = MakeExpression.generate_expression()
        if expr == None:
            continue
        inequality = ["= 1", "> 1", "< 1", ">= 1", "<= 1"]
        sign_to_latex = {"= 1" : "= 1", "> 1" : "> 1", "< 1": "< 1", ">= 1": "\\geq 1", "<= 1" : "\\leq 1"}
        index = random.randint(0, 4)
        latex += " " + sign_to_latex[inequality[index]]
        sign = inequality[index]
        loc = folder + "\\equation" + str(count + 1) + ".png"
        make_img("$" + latex + "$", loc)
        return render_template("FindMany.html", src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)
 
@app.route('/ValidateMany')
def ValidateMany():
    global start
    start = time.time()
    satisfies = Validator.valid(symbol_set, expr, index)
    save(satisfies)
    return render_template("ValidateMany.html", satisfies=satisfies, src = loc, eq = (valid + invalid), valid = valid, invalid = invalid, vtime = avg_valid_time, itime = avg_invalid_time)


@app.route('/Previous')
@app.route('/Previous/<filters>')
def Previous(filters = None):
    global filt
    if filters == None:
        filt = False
        return render_template("Previous.html")
    else:
        filt = True
        filters = filters.split("-")
        validity_filters = set()
        term_filters = set()
        for i in filters:
            if i in ["invalid", "equilateral", "scalene", "isosceles", "right"]:
                validity_filters.add(i)
            if i in ["a", "b", "c", "s", "r", "R", "m_A", "m_B", "m_C", "h_A", "h_B", "h_C", "T"]:
                term_filters.add(sympy.Symbol(i))
            if i in ["A", "B", "C"]:
                term_filters.add(sympy.cos(sympy.Symbol(i)))
                term_filters.add(sympy.sin(sympy.Symbol(i)))
        filtered = [i for i in range(len(all_equations))]
        if len(validity_filters) > 0:
            for index, eq in enumerate(all_equations):
                validity = []
                if eq[0] == "invalid":
                    validity = ["invalid"]
                else:
                    validity = [i for i in eq[0].split(", ")]
                for t in validity:
                    if t not in validity_filters:
                        filtered.remove(index)
                        break
        if len(term_filters) > 0:
            for ind in filtered.copy():
                for term in term_filters:
                    if term not in all_equations[ind][4]:
                        filtered.remove(ind)
        print(filtered)
        return render_template("Previous.html", filtered=filtered )

        

            
        #Make type be a list of all the types (i.e. ["invalid"] or ["equialteral, isosceles"])
        

        return ""


@app.route('/Equations')
def Equations():
    global all_equations, run_once
    if run_once == True:
        l = [[i[0], i[5], i[6]] for i in all_equations]
        output = {"": l}
        return jsonify(output)
    else:
        all_equations = []
        if filt == False:
            clear()
        equations = BackToSympy.getPastInequalities()
        l = []
        for i in range(0, len(equations)):
            type = equations[i][0]
            if type != "invalid":
                type = ", ".join([t[t.index("\"")+1:t.rindex("\"")] for t in type.split(",")])
            latex = equations[i][2]
            folder = "static\\images\\storage\\"
            name = "image" + str(i) + ".png"
            all_equations.append((type, latex, equations[i][1], equations[i][4], equations[i][5], name, equations[i][3]))
            make_img(latex, folder + name)
            l.append([type, name, equations[i][3]])
        run_once = True
        output = {"" : l}
        return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


def expression_finder():
    global valid, invalid
    start = time.time()
    expr, latex, symbol_set = MakeExpression.generate_expression()
    if expr != "":
        inequality = ["= 1", "> 1", "< 1", ">= 1", "<= 1"]
        sign_to_latex = {"= 1" : "= 1", "> 1" : "> 1", "< 1": "< 1", ">= 1": "\\geq 1", "<= 1" : "\\leq 1"}
        i = random.randint(0, 4)
        satisfies = Validator.valid(symbol_set, expr, i)
        if satisfies != False:
            valid += 1
            folder = "Valid"
            latex += " " + sign_to_latex[inequality[i]]
            """ print(latex)
            print(satisfies) """
            make_img("$" + latex + "$", valid, folder)
            return "Website\\static\\images\\equations\\" + folder + "\\equation" + str(valid) + ".png", time.time() - start
        else:
            invalid += 1
            folder = "Invalid"
            latex += " " + sign_to_latex[inequality[i]]
            """ print(latex)
            print(satisfies) """
            make_img("$" + latex + "$", invalid, folder)
            return ("Website\\static\\images\\equations\\" + folder + "\\equation" + str(invalid) + ".png", time.time() - start)
    
    




