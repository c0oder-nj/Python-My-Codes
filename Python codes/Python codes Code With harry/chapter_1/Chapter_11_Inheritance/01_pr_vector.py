class C2dVec:
    def __init__(self, i ,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

Vec2d = C2dVec(4,5)
print(Vec2d)

vec3d = C3dVec(6,8,12)
print(vec3d)
