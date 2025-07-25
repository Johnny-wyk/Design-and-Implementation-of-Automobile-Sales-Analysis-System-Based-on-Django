#coding:utf-8

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.apps import apps

from util.auth import Auth
from util.codes import *
from 汽车销量分析系统.settings import dbName as schemaName


class Xauth(MiddlewareMixin):
    def process_request(self,request):
        fullPath = request.get_full_path()
        print("fullPath===============>", fullPath)
        if request.META.get('HTTP_UPGRADE')=='websocket':
            return
        if request.method == 'GET':

            filterList=[
                "/index",
                "/follow",
                "/favicon.ico",
                "/login",
                "/register",
                "/notify",
                "/file",
                '.js',
                ".css",
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".mp4",
                '.mp3',
                ".ttf",
                ".wotf",
                ".woff",
                ".woff2",
                ".otf",
                ".eot",
                ".svg",
                ".csv",
                ".webp",
                ".xls",
                ".xlsx",
                ".doc",
                ".docx",
                ".ppt",
                ".pptx",
                ".html",
                ".htm",
                "detail",
                "/forum/flist",
                "/forum/list",
                "/admin",
                "/security",
                "/autoSort",
                "/config/list",
                "/news/list",
                "/xadmin",
                "/file/download",
                 "/{}/remind/".format(schemaName),
                  "/{}/option/".format(schemaName),
                "resetPass",
                "updateBrowseDuration",
            ]

            allModels = apps.get_app_config('main').get_models()
            # print("allModels:",allModels.)
            for m in allModels:
                try:
                    foreEndList=m.__foreEndList__
                except:
                    foreEndList=None
                if  foreEndList is None or foreEndList != "前要登":
                    filterList.append("/{}/sendemail".format(m.__tablename__))
                    filterList.append("/{}/sendsms".format(m.__tablename__))
                    filterList.append("/{}/list".format(m.__tablename__))
                    filterList.append("/{}/detail".format(m.__tablename__))

            auth = True

            if fullPath=='/':
                pass
            else:
                for i in filterList:
                    if i in fullPath:
                        auth=False
                if auth==True:
                    result = Auth.identify(Auth, request)

                    if result.get('code') != normal_code:
                        return JsonResponse(result)
        elif request.method == 'POST':
            post_list = [
                '/{}/defaultuser/register'.format(schemaName),
                '/{}/defaultuser/login'.format(schemaName),
                '/{}/users/register'.format(schemaName),
                '/{}/users/login'.format(schemaName),
                "/{}/examusers/login".format(schemaName),
                "/{}/examusers/register".format(schemaName),
                "/{}/file/upload".format(schemaName),
                "/update"
            ]  # 免认证list
            if fullPath not in post_list and "register" not in fullPath and "login" not in fullPath and "faceLogin" not in fullPath and "update" not in fullPath and "upload" not in fullPath:  # 注册时不检测token。
                result = Auth.identify(Auth, request)

                if result.get('code') != normal_code:
                    print('jwt auth fail')
                    return JsonResponse(result)
