import os

def rearrange(edges):
    edges = edges[1:-1].split(',')
    for i in range(len(edges)):
        if edges[i][:2] == '1-':
            subFirst = edges[:i]
            subRest = edges[i:]
            result = subRest+subFirst
            for j in range(len(result)):
                vertex = result[j].split("-")[0]
                result[j] = vertex
            result.append("0")
            result =  " ".join(map(str,result))
            return result

rand = os.getcwd() + "\\rand"
for instanceDir in os.scandir(rand):
    for instance in os.scandir(instanceDir):
        instancePath = rand + "\\" + instanceDir.name + "\\" + instance.name

        f = open(instancePath,"r")
        #prepare the <instance>.hamsol filename, which will be located inside the results folder
        resName = instancePath.split("\\")
        resName = resName[-1]
        instanceName = resName
        resName = "results//" + resName.split(".ham")[0] + ".hamsol"
        lines = f.readlines()
        for line in lines:
            line = line.split()
            #find the provided answer
            if line[0] == 'c' and len(line) > 1 and line [1][0] == "[":
                edges = line[1]
                # print(edges)
                edges = rearrange(edges)
                os.system("python bonus1.py " + instancePath)
                f = open(resName,"r")
                instanceSol = f.readline()
                if edges == instanceSol:
                    print("instance: " + instanceName + " PASSED!")
                else:
                    print("instance " + instanceName + " returned: " + instanceSol)
