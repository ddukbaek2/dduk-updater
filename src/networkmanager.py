#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, Tuple, List, Dict, Set, cast
import builtins
from http import HTTPStatus
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template
from dduk.core import Repository
from src.datamanager import DataManager
from src.commandmanager import CommandManager


#--------------------------------------------------------------------------------
# 네트워크 매니저.
#--------------------------------------------------------------------------------
class NetworkManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__app : Flask


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__app = Flask("DDUK-UPDATER")
		self.__app.add_url_rule("/", "OnRequest", self.OnRequest, methods = ["GET"])
		# self.__app.add_url_rule("/", "RequestDefault", self.RequestDefault, methods = ["GET"])
		# self.__app.add_url_rule("/execute", "RequestExecute", self.RequestExecute, methods = ["GET"])
		# self.__app.add_url_rule("/kill", "RequestKill", self.RequestKill, methods = ["GET"])


	#--------------------------------------------------------------------------------
	# 서버 시작.
	#--------------------------------------------------------------------------------
	def Run(self, host : str, port : int) -> None:
		self.__app.run(host = host, port = port)


	#--------------------------------------------------------------------------------
	# 프로세스 시작.
	#--------------------------------------------------------------------------------
	def OnRequest(self) -> Union[str, Tuple[str, int]]:
		try:
			cmd : str = request.args.get("cmd")
			builtins.print(f"cmd: {cmd}")

			cmds = cmd.split()
			command = cmds[0]
			builtins.print(f"command: {command}")
			arguments = cmds[1:]
			builtins.print(f"arguments: {command}")

			commandManager : CommandManager = Repository.Get(CommandManager)
			output = commandManager.Start(command, arguments)
			return output, HTTPStatus.OK
		except Exception as exception:
			return str(exception), HTTPStatus.INTERNAL_SERVER_ERROR


	# #--------------------------------------------------------------------------------
	# # 아무 요청 안함.
	# #--------------------------------------------------------------------------------
	# def RequestDefault(self) -> Union[str, Tuple[str, int]]:
	# 	return "", HTTPStatus.OK


	# #--------------------------------------------------------------------------------
	# # 프로세스 시작.
	# #--------------------------------------------------------------------------------
	# def RequestExecute(self) -> Union[str, Tuple[str, int]]:
	# 	try:
	# 		command = request.args.get("cmd")
	# 		commands = command.split(",")
	# 		executeFilePath = commands[0]
	# 		builtins.print(executeFilePath)
	# 		commandManager : CommandManager = Repository.Get(CommandManager)
	# 		commandManager.Execute(executeFilePath)
	# 		return "", HTTPStatus.OK
	# 	except Exception as exception:
	# 		return str(exception), HTTPStatus.INTERNAL_SERVER_ERROR


	# #--------------------------------------------------------------------------------
	# # 프로세스 파괴.
	# #--------------------------------------------------------------------------------
	# def RequestKill(self) -> Union[str, Tuple[str, int]]:
	# 	try:
	# 		command = request.args.get("cmd")
	# 		commands = command.split(",")
	# 		processName : str = commands[0]
	# 		killRootPath : str = commands[1]
	# 		commandManager : CommandManager = Repository.Get(CommandManager)
	# 		commandManager.Kill(processName, killRootPath)
	# 		return "", HTTPStatus.OK
	# 	except Exception as exception:
	# 		return str(exception), HTTPStatus.INTERNAL_SERVER_ERROR