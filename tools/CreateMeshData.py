'''
Author: chuzeyu 3343447088@qq.com
Date: 2023-07-19 09:48:14
LastEditors: chuzeyu 3343447088@qq.com
LastEditTime: 2023-07-19 14:38:13
FilePath: \three-vehicle\tools\CreateMeshData.py
Description: python小工具,用于预处理glb数据
'''
import trimesh
import json

#将glb模型转为生成trimesh数据的参数vertices、faces
def get_v_f_from_glb():
    scene = trimesh.load('F:/yun/three-vehicle/static/models/road/road_cons.glb')
    geometries = list(scene.geometry.values())
    geometry = geometries[0]
    v = geometry.vertices
    f = geometry.faces
    return v, f

def saveJson(path, data):
    f2 = open(path, 'w')
    f2.write(data)
    f2.close()

if __name__ == '__main__':
    v, f = get_v_f_from_glb()
    saveJson('./v.json', json.dumps(v.tolist()))
    saveJson('./f.json', json.dumps(f.tolist()))