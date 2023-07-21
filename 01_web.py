#!/opt/eenos/python39/bin/python3
from pprint import pprint
class Data:
    def __init__(self,data=None,name=None):
        default_data = {
            "id": "1",
            "name": "first",
            "metadata": {
                "system": {
                    "size": 10.7
                },
                "user": {
                    "batch": 10
                }
            }
        }
        if not data:
            data=default_data        
        self.data=data 
        if name:
            self.data['name']=name
            input_size=input("Enter System size  for ' %s '(Default : 10 ): " %name)            
            if bool(input_size) and str(input_size).isnumeric():
                self.data['metadata']['system']['size']=input_size
            else:
                self.data['metadata']['system']['size']=10
            input_batch=input("Enter user batch  for ' %s ' (Default batch : 10): " %name)            
            if bool(input_batch) and str(input_batch).isnumeric():
                self.data['metadata']['user']['batch']=input_size
            else:
                self.data['metadata']['user']['batch']=10            

        if 'metadata' in self.data and 'system' in self.data['metadata'] and 'size' in self.data['metadata']['system'] and bool(self.data['metadata']['system']['size']):
            self.size=int(self.data['metadata']['system']['size'])
        else:
            self.size=0
          
        if 'metadata' in self.data and 'system' in self.data['metadata'] and 'height' in self.data['metadata']['system'] and bool(self.data['metadata']['system']['height']):
            self.height=int(self.data['metadata']['system']['height'])
        else:
            self.data['metadata']['system']['height']=100
            self.height=100
        self.metadata=self.data['metadata']
        self.id=self.data['id']    
        self.name=self.data['name']      
        

    @classmethod
    def from_dict(cls,data=None):
        return cls(data)

    def to_dict(self):
        return self.data


if __name__ == "__main__":   
    # This dictionary can be used to load data from dictionary
    input_data = {
        "id": "2",
        "name": "second",
        "metadata": {
            "system": {
                "size": 11.7,
                # "height": 200,
            },
            "user": {
                "batch": 11
            }
        }
    }

   # load from dict
    my_inst_1=Data.from_dict(input_data)
    # load from inputs
    my_inst_2 = Data(name="my")
    # reflect inner value
    print('# reflect inner value')
    print(my_inst_1.size)  # should print 10
        
    # default values 
    print('# default values')
    print(my_inst_1.height)  # should set a default value of 100 in metadata.system.height   
    print(my_inst_1.to_dict()['metadata']['system']['height'])  # should print the default value
    # Autocomplete 
    print(" # Autocomplete - You  mean the final data ?")
    pprint (my_inst_1.data)
    pprint (my_inst_2.data)
