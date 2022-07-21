import platform
import os

print ('Version      :', platform.python_version())
print ('Version tuple:', platform.python_version_tuple())
print ('Compiler     :', platform.python_compiler())
print ('Build        :', platform.python_build())


print ('Normal :', platform.platform())
print ('Aliased:', platform.platform(aliased=True))
print ('Terse  :', platform.platform(terse=True))


if "Windows" in platform.platform():
    print("Windows System")
elif "redhat" in platform.platform():
    print("Redhat System")
    os.system("sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo")
    os.system("sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key")
    os.system("sudo yum upgrade")
    # Add required dependencies for the jenkins package
    os.system("sudo yum install java-11-openjdk")
    os.system("sudo yum install jenkins")
    os.system("sudo systemctl daemon-reload")
    
elif "ubuntu" in platform.platform():
    print("Ubuntu system")
    os.system("curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null")
    os.system("echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install jenkins")
