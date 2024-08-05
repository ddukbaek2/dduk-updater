#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
import os
import sys
from dduk.core import Repository


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
EMPTY : str = ""
FROZEN : str = "frozen"
MAIN : str = "__main__"
BACKSLASH : str = "\\"
SLASH : str = "/"
CURRENTFILEPATH : str = os.path.abspath(__file__)
SRCPATH : str = os.path.dirname(CURRENTFILEPATH).replace(BACKSLASH, SLASH)


#--------------------------------------------------------------------------------
# 빌드 여부.
#--------------------------------------------------------------------------------
def IsBuild() -> bool:
	# 실행 환경 체크.
	try:
		return builtins.getattr(sys, FROZEN, False)
	except Exception as exception:
		return False


#--------------------------------------------------------------------------------
# 파일 진입점.
#--------------------------------------------------------------------------------
if __name__ == MAIN:

	# 출력.
	builtins.print("__LAUNCHER__")

	if IsBuild():
		cachePath : str = sys._MEIPASS
		rootPath : str = os.path.dirname(sys.executable)
		sourcePath : str = os.path.join(cachePath, "src")
		resourcePath : str = os.path.join(cachePath, "res")
		workspacePath : str = rootPath
	else:
		# currentFilePath = os.path.abspath(__file__)
		# sourcePath = os.path.dirname(currentFilePath)
		currentFilePath = os.path.abspath(sys.modules[MAIN].__file__)
		sourcePath : str = os.path.dirname(currentFilePath) 
		rootPath : str = os.path.dirname(sourcePath)
		resourcePath : str = os.path.join(rootPath, "res")
		workspacePath : str = os.path.join(rootPath, "workspace")

		# 코드 추가.
		if rootPath and rootPath not in sys.path: sys.path.append(rootPath)
		if sourcePath and sourcePath not in sys.path: sys.path.append(sourcePath)

	# 변수 설정.
	from src.datamanager import DataManager
	dataManager : DataManager = Repository.Get(DataManager)

	# 경로 추가.
	dataManager.SetRootPath(rootPath)
	dataManager.SetResourcePath(resourcePath)
	dataManager.SetSourcePath(sourcePath)
	dataManager.SetWorkspacePath(workspacePath)

	# 시작.
	from src.__main__ import Main
	Main(sys.argv)
