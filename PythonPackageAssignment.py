# %%
pip install httpimport


# %%
import httpimport
url = "https://github.com/adam2909/PythonPackage"
httpimport.INSECURE =True
with httpimport.remote_repo(url):
  import PythonFunctions
print(PythonFunctions.evenOdd(4))


