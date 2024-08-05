#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Final, Optional, Type, TypeVar, Union, Tuple, Callable, Any, List, Dict, Set, cast
import builtins
import json
import os


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
DEFAULT_HOST : str = "0.0.0.0"
DEFAULT_PORT : int = 5000
READ : str = "r"
UTF8 : str = "utf-8"
HOST : str = "host"
PORT : str = "port"
SERVER : str = "server"
EXECUTABLEPATH : str = "executablePath"


#--------------------------------------------------------------------------------
# 매니페스트 해석기.
#--------------------------------------------------------------------------------
class ManifestParser:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	Host : str
	Port : int
	Services : dict[str, str] # name, path


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.Host = DEFAULT_HOST
		self.Port = DEFAULT_PORT
		self.Services = dict()


	#--------------------------------------------------------------------------------
	# 해석.
	#--------------------------------------------------------------------------------
	def Parse(self, manifestFilePath : str) -> bool:
		try:
			if not os.path.isfile(manifestFilePath):
				return False			
			with open(manifestFilePath, READ, encoding = UTF8) as file:
				jsonManifestData : dict = json.load(file)
				if not jsonManifestData:
					return False			
				if SERVER in jsonManifestData:
					jsonServerData : dict = jsonManifestData.get(SERVER, {HOST : DEFAULT_HOST, PORT : DEFAULT_PORT })
					self.Host = jsonServerData.get(HOST, DEFAULT_HOST)
					self.Port = jsonServerData.get(PORT, DEFAULT_PORT)
			return True		
		except Exception as exception:
			builtins.print(exception)
			return False