
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
class ChartSubModule:
    # constructor
    def __init__(self, module_type : str, module_json : list):
        self.data = module_json
        pass
    
    # def to_json(self):

class ChartModule:
    # constructor
   def __init__(self, dataset:list):
    #    "2020-07-20","2020-07-21","2020-07-22","2020-07-23","2020-07-24",
        self.labels = dataset[len(dataset)-1]
        print("Created chart support module")
        subModules = []
        for data in dataset:
            if(dataset.index(data)!=len(dataset)-1):
                subModule = ChartSubModule('line', data)
                subModules.append(subModule)
        self.submodules = subModules
        pass
