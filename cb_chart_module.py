
import json
import html

# datasets_list = [{
#         label: "Europe",
#         type: "line",
#         borderColor: "#8e5ea2",
#         data: [408, 547, 675, 734],
#         fill: false
#     }, {
#         label: "Africa",
#         type: "line",
#         borderColor: "#3e95cd",
#         data: [133, 221, 783, 2478],
#         fill: false
#     }, {
#         label: "Europe",
#         type: "bar",
#         backgroundColor: "rgba(0,0,0,0.2)",
#         data: [408, 547, 675, 734],
#     }, {
#         label: "Africa",
#         type: "bar",
#         backgroundColor: "rgba(0,0,0,0.2)",
#         backgroundColorHover: "#3e95cd",
#         data: [133, 221, 783, 2478]
#     }]

class ChartSubModule_Line:
    # constructor
    def __init__(self, module_json : list):
        self.data = {}
        print("Created chart support sub module {}".format(ChartSubModule.TYPE_LINE))
        for key in module_json:
            self.data[key] = module_json[key] 
        pass

class ChartSubModule_Bar:
    # constructor
    def __init__(self, module_json : list):
        self.data = {}
        print("Created chart support sub module {}".format(ChartSubModule.TYPE_BAR))
        for key in module_json:
            self.data[key] = module_json[key]
        pass

class ChartSubModule:    
    TYPE_LINE = "line"
    TYPE_BAR = "bar"
    # constructor
    def __init__(self, module_type : str, module_json : list):
        subModule = None
        self.data = {}
        if(module_type == "line"):
            subModule = ChartSubModule_Line(module_json) 
        else:
            subModule = ChartSubModule_Bar(module_json)    
        self.data = subModule.data
        pass
    
    # def to_json(self):

class ChartModule:
    # constructor
    def __init__(self, dataset:list):
        self.labels = [1900, 1950, 1999, 2050, 2100]
        print("Created chart support module")
        submodules = []
        for data in dataset:
            subModule = ChartSubModule(data['type'], data)
            submodules.append(subModule.data)
        self.submodules = submodules
        print(submodules)
        pass
