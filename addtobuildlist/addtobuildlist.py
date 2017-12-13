import sys
import os
import hglib
import subprocess

def main(argv):
  repoPath = argv[0]
  repo = hglib.open(repoPath)
  statusList = repo.status()
  linkSet = createLinkList(statusList)
  for link in linkSet:
    modulePath = os.path.dirname(link)
    subsystem = os.path.basename(link)
    linkSourceFolder = os.path.join(b'w:\\TestLab\\Cada-NT\\',modulePath).decode()
    if not os.path.exists(linkSourceFolder):
      os.makedirs(linkSourceFolder)
    assert(os.path.exists(linkSourceFolder))
    
    linkSource = os.path.join(linkSourceFolder, subsystem.decode())

    linkTarget = os.path.join(repoPath,'Cada-NT', modulePath.decode(), subsystem.decode())
    assert(os.path.exists(linkTarget))
    #win32file.CreateSymbolicLink(linkSource,linkTarget, 0)
    localSubsystemsFile = open("W:\\local_subsystems.txt", 'a')
    if not os.path.exists(linkSource):
      command = "mklink /D " + linkSource + " " + linkTarget
      subprocess.call(command, shell = True)
      localSubsystemsFile.write(link.decode() + "\n")
    localSubsystemsFile.close()
  print(linkSet)

def createLinkList(statusList):
  linkSet = set()
  for status in statusList:
    filePath = status[1]
    linkSet.add(createLink(filePath))
  return linkSet

def createLink(filePath):
  directories = filePath.rsplit(b'\\')
  #                           LmsHq           Module          Subsystem
  relativePath = os.path.join(directories[1], directories[2], directories[3])
  return relativePath

if __name__ == '__main__':
    main(sys.argv[1:])
