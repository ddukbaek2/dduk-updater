#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"


#--------------------------------------------------------------------------------
# 데이터 매니저.
#--------------------------------------------------------------------------------
class DataManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__rootPath : str
	__resourcePath : str
	__sourcePath : str
	__workspacePath : str


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__rootPath = str()
		self.__resourcePath = str()
		self.__sourcePath = str()
		self.__workspacePath = str()


	#--------------------------------------------------------------------------------
	# 루트 경로 설정.
	#--------------------------------------------------------------------------------
	def SetRootPath(self, rootPath : str) -> None:
		self.__rootPath = rootPath.replace(BACKSLASH, SLASH)
	
	
	#--------------------------------------------------------------------------------
	# 리소스 경로 설정.
	#--------------------------------------------------------------------------------
	def SetResourcePath(self, resourcePath : str) -> None:
		self.__resourcePath = resourcePath.replace(BACKSLASH, SLASH)
	

	#--------------------------------------------------------------------------------
	# 소스 경로 설정.
	#--------------------------------------------------------------------------------
	def SetSourcePath(self, sourcePath : str) -> None:
		self.__sourcePath = sourcePath.replace(BACKSLASH, SLASH)
	
	
	#--------------------------------------------------------------------------------
	# 워크스페이스 경로 설정.
	#--------------------------------------------------------------------------------
	def SetWorkspacePath(self, workspacePath : str) -> None:
		self.__workspacePath = workspacePath.replace(BACKSLASH, SLASH)


	#--------------------------------------------------------------------------------
	# 루트 경로 반환.
	#--------------------------------------------------------------------------------
	def GetRootPath(self) -> str:
		return self.__rootPath


	#--------------------------------------------------------------------------------
	# 리소스 경로 반환.
	#--------------------------------------------------------------------------------
	def GetResourcePath(self) -> str:
		return self.__resourcePath
	

	#--------------------------------------------------------------------------------
	# 소스 경로 반환.
	#--------------------------------------------------------------------------------
	def GetSourcePath(self) -> str:
		return self.__sourcePath
	

	#--------------------------------------------------------------------------------
	# 워크스페이스 경로 반환.
	#--------------------------------------------------------------------------------
	def GetWorkspacePath(self) -> str:
		return self.__workspacePath
	

	#--------------------------------------------------------------------------------
	# 루트 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetRootPathWithRelativePath(self, relativePath : str) -> str:
		rootPath = self.GetRootPath()
		if not os.path.isdir(rootPath): os.makedirs(rootPath)
		if not relativePath:
			return rootPath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{rootPath}/{relativePath}"
		return absolutePath		
	

	#--------------------------------------------------------------------------------
	# 리소스 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetResourcePathWithRelativePath(self, relativePath : str) -> str:
		resourcePath = self.GetResourcePath()
		if not os.path.isdir(resourcePath): os.makedirs(resourcePath)
		if not relativePath:
			return resourcePath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{resourcePath}/{relativePath}"
		return absolutePath
	

	#--------------------------------------------------------------------------------
	# 소스 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetSourcePathWithRelativePath(self, relativePath : str) -> str:
		sourcePath = self.GetSourcePath()
		if not os.path.isdir(sourcePath): os.makedirs(sourcePath)
		if not relativePath:
			return sourcePath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{sourcePath}/{relativePath}"
		return absolutePath
	

	#--------------------------------------------------------------------------------
	# 워크스페이스 경로를 기반으로 상대경로를 추가하여 반환.
	#--------------------------------------------------------------------------------
	def GetWorkspacePathWithRelativePath(self, relativePath : str) -> str:
		workspacePath = self.GetWorkspacePath()
		if not os.path.isdir(workspacePath): os.makedirs(workspacePath)
		if not relativePath:
			return workspacePath
		relativePath = relativePath.replace(BACKSLASH, SLASH)
		absolutePath = f"{workspacePath}/{relativePath}"
		return absolutePath