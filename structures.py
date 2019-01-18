# Define all usable structures in this file
# Global Params will be defined as an accessable array with an undetermined length,
# so that the user can define as many parameters as they wish.
global_params = []

# Jobs will be an array of all user defined jobs for easier access and tracking of specific jobs: structure:: [usrjob0,usrjob1,usrjob2,....]
Jobs = []

# usrjob is an array that will be filled with user parameters: structure:: ['[name of job]',job_params[]]
usrjob = []

# job_params parameters will be defined as an array containing all job parameters: structure:: [param1, param2, param3,....]
job_params = []

defaults = ['[global]',Jobs]