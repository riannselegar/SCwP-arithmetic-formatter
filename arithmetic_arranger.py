def arithmetic_arranger(problems, sum=False):
    firstLine = ''
    secondLine = ''
    thirdLine = ''
    fourthLine = ''

    if len(problems) > 5:
        return "Error: Too many problems."

    for exp in problems:
        splited = exp.split()
        if max(len(splited[0]), len(splited[2])) > 4:
            return "Error: Numbers cannot be more than four digits."
        if splited[1] != '+' and splited[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not splited[0].isnumeric() or not splited[2].isnumeric():
            return "Error: Numbers must only contain digits."

        firstLine += splited[0].rjust(max(len(splited[0]), len(splited[2])) + 2) + ''.rjust(4)
        secondLine += splited[1] + splited[2].rjust(max(len(splited[0]), len(splited[2])) + 1) + ''.rjust(4)
        thirdLine += ''.rjust(max(len(splited[0]), len(splited[2])) + 2, "-") + ''.rjust(4)
        if sum:
            tmpSum = eval(f'{int(splited[0])} {splited[1]} {int(splited[2])}')
            fourthLine += str(tmpSum).rjust(max(len(splited[0]), len(splited[2])) + 2) + ''.rjust(4)

    firstLine = firstLine.rstrip() + '\n'
    secondLine = secondLine.rstrip() + '\n'
    thirdLine = thirdLine.rstrip() + '\n'

    arranged_problems = (firstLine + secondLine + thirdLine + fourthLine).rstrip()

    return arranged_problems