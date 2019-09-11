# Readme File 
1. For running a test, create file with format 
`test_<name>.py` in folder <b>tests</b> and execute command 
`pytest tests/test_<name>.py`

2. For running all tests of folder `tests`, 
run `pytest tests/`

3. To run a specific function inside a test, call 
`pytest test_mod.py::test_func`

#Add Marker 
if you want to run a specif no of tests only, add marker.
You can find examples in test folder, 
To run all tests with marker `slow`, call 
`pytest -m slow`
