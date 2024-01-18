"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os
for i in range(2, 11, 2):
    old = f"C:\PycharmProjects\pythonProject2\PythonTasks/ModuleOS/target/{i}"
    new = f"C:\PycharmProjects\pythonProject2\PythonTasks/ModuleOS/target/am_{i}"
    os.rename(old, new)