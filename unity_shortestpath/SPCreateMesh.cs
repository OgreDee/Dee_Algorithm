using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;


#if UNITY_EDITOR
using UnityEditor;

[CustomEditor(typeof(SPCreateMesh))]
public class SPCreateMeshEditor : Editor
{
    public override void OnInspectorGUI()
    {
        base.OnInspectorGUI();

        if(GUILayout.Button("Mesh Gen"))
        {
            (target as SPCreateMesh).GeneratorMesh();
        }

        if (GUILayout.Button("DijkstraPathFinding"))
        {
            (target as SPCreateMesh).DijkstraPathFindingFunc();
        }
        if (GUILayout.Button("Clean Path"))
        {
        }
    }
}
#endif


public enum CellStatus : byte
{
    Empty = 0 << 1,         //空格子
    Obstacle = 1 << 1,      //障碍
    StartCell = 2 << 1,     //起点
    TargetCell = 3 << 1,    //目标点
}

public class SPCreateMesh : MonoBehaviour
{
    [SerializeField]
    Mesh mesh;
    [SerializeField]
    Vector2Int size;
    [SerializeField]
    Vector2Int startPos;
    [SerializeField]
    Vector2Int targetPos;

    [SerializeField][Range(0.01f, 0.3f)]
    float offset = 0.05f;

    Color emptyColor = Color.gray;
    Color startColor = Color.green;
    Color targetColor = Color.blue;

    //格子状态
    CellStatus[,] arr_status;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    public void DijkstraPathFindingFunc()
    {
        var helper = new DijkstraPathFinding();
        helper.Excute(startPos, targetPos, arr_status);
        if(helper.HasPathTo(targetPos))
        {
            var path = helper.PathTo(targetPos);
            //foreach(var c in path)
            //{
            //    Debug.Log(c);
            //}
            Color color = Color.yellow;
            var colors = mesh.colors;
            foreach (var p in path)
            {
                if(p != startPos && p != targetPos)
                {
                    int vertexIdx = p.y * size.x * 4 + p.x * 4;
                    colors[vertexIdx + 0] = color;
                    colors[vertexIdx + 1] = color;
                    colors[vertexIdx + 2] = color;
                    colors[vertexIdx + 3] = color;
                }
            }
            mesh.colors = colors;
        }
        else
        {
            //路径不通
            Debug.LogError("路径不通....");
        }
    }


    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Camera cam = Camera.main;
            Vector3 worldPos = cam.ScreenToWorldPoint(Input.mousePosition);
            Vector3 localPos = transform.InverseTransformPoint(worldPos);

            int row = Mathf.Clamp(Mathf.FloorToInt(localPos.y), 0, size.y-1);
            int col = Mathf.Clamp(Mathf.FloorToInt(localPos.x), 0, size.x-1);
            arr_status[col, row] = CellStatus.Obstacle;

            Color color = Color.red;
            var colors =  mesh.colors;
            int vertexIdx = row * size.x * 4 + col * 4;
            colors[vertexIdx + 0] = color;
            colors[vertexIdx + 1] = color;
            colors[vertexIdx + 2] = color;
            colors[vertexIdx + 3] = color;
            mesh.colors = colors;
        }
    }

    private void OnValidate()
    {
        
    }

    [ContextMenu("Mesh Gen")]
    public void GeneratorMesh()
    {
        if(mesh == null)
        {
            mesh = new Mesh();
            mesh.name = "dee mesh";
            mesh.MarkDynamic();
            mesh.hideFlags = HideFlags.DontSave;
        }

        int[] triangles = new int[size.x * size.y * 6];
        Vector3[] vertices = new Vector3[size.x * size.y * 4];
        Color[] colors = new Color[size.x * size.y * 4];
        arr_status = new CellStatus[size.x, size.y]; 

        for (int y = 0; y < size.y; y++)
        {
            for (int x = 0; x < size.x; x++)
            {
                //生成一个quad(6个顶点构成)
                Vector3 v0 = new Vector3();
                v0.x = x + offset;
                v0.y = y + offset;
                Vector3 v1 = new Vector3();
                v1.x = x + 1 - offset;
                v1.y = y + offset;
                Vector3 v2 = new Vector3();
                v2.x = x + 1 - offset;
                v2.y = y + 1 - offset;
                Vector3 v3 = new Vector3();
                v3.x = x + offset;
                v3.y = y + 1 - offset;

                int vIdx = y * size.x * 4 + x * 4;
                vertices[vIdx + 0] = v0;
                vertices[vIdx + 1] = v1;
                vertices[vIdx + 2] = v2;
                vertices[vIdx + 3] = v3;
                colors[vIdx + 0] = emptyColor;
                colors[vIdx + 1] = emptyColor;
                colors[vIdx + 2] = emptyColor;
                colors[vIdx + 3] = emptyColor;

                int tIdx = x * size.y * 6 + y * 6;
                triangles[tIdx + 0] = vIdx + 0;
                triangles[tIdx + 1] = vIdx + 3;
                triangles[tIdx + 2] = vIdx + 1;
                triangles[tIdx + 3] = vIdx + 3;
                triangles[tIdx + 4] = vIdx + 2;
                triangles[tIdx + 5] = vIdx + 1;

                arr_status[x, y] = CellStatus.Empty;
            }
        }


        //点的color
        int vertexIdx = startPos.y * size.x * 4 + startPos.x * 4;
        colors[vertexIdx + 0] = startColor;
        colors[vertexIdx + 1] = startColor;
        colors[vertexIdx + 2] = startColor;
        colors[vertexIdx + 3] = startColor;

        vertexIdx = targetPos.y * size.x * 4 + targetPos.x * 4;
        colors[vertexIdx + 0] = targetColor;
        colors[vertexIdx + 1] = targetColor;
        colors[vertexIdx + 2] = targetColor;
        colors[vertexIdx + 3] = targetColor;


        mesh.Clear(false);
        mesh.vertices = vertices;
        mesh.colors = colors;
        mesh.SetTriangles(triangles, 0);
        GetComponent<MeshFilter>().mesh = mesh;
        GetComponent<MeshCollider>().sharedMesh = mesh;

        transform.position = new Vector3(-size.x * 0.5f, -size.y * 0.5f, 5);
        Camera.main.orthographicSize = Mathf.Max(size.x, size.y) * 0.6f;

    }
}
