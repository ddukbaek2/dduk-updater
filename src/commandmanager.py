#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import subprocess
import sys
from dduk.core import Repository
from dduk.utils import strutil
from dduk.process.processinfo import ProcessInfo
from dduk.process.processmanager import ProcessManager
from src.datamanager import DataManager

#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
BACKSLASH : str = "\\"
SLASH : str = "/"


#--------------------------------------------------------------------------------
# 커맨드 매니저.
#--------------------------------------------------------------------------------
class CommandManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		pass

	#--------------------------------------------------------------------------------
	# 프로세스 생성.
	#--------------------------------------------------------------------------------
	def Execute(self, executeFilePath : str) -> None:
		try:
			process = subprocess.Popen([executeFilePath], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
		except Exception as exception:
			builtins.print(exception)

	#--------------------------------------------------------------------------------
	# 프로세스 파괴.
	#--------------------------------------------------------------------------------
	def Kill(self, processName : str, killRootPath : str) -> None:
		dataManager : DataManager = Repository.Get(DataManager)
		processManager : ProcessManager = Repository.Get(ProcessManager)
		
		killRootPath = killRootPath.replace(BACKSLASH, SLASH)
		builtins.print(f"killRootPath={killRootPath}")

		processInfos : dict[int, ProcessInfo] = processManager.FindProcessInfosByName(processName)
		for processID, processInfo in processInfos.items():
			processInfo = cast(ProcessInfo, processInfo)
			executeFilePath = processInfo.FilePath.replace(BACKSLASH, SLASH)
			executeFilePath = executeFilePath.upper()
			if killRootPath in executeFilePath:
				builtins.print(f"processID={processID}, FilePath={executeFilePath}")
				try:
					if processManager.DestroyProcessImmediateByID(processInfo.ID):
						builtins.print(f"Process Kill: {processInfo.ID}")
					else:
						builtins.print(f"Process Kill Failed: {processInfo.ID}")
				except Exception as exception:
					builtins.print(f"Process Kill Exception: {processInfo.ID}, exception={exception}")