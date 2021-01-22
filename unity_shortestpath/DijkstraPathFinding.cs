using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DijkstraPathFinding
{
    int mMapWidth;
    int mMapHeight;
    Vector2Int mStartPos;
    int mStartIdx;

    int[] edgeTo;
    int[] distTo;
    Queue<Vector2Int> openList;


    public bool HasPathTo(Vector2Int target)
    {
        return distTo[CalculateIdx(ref target)] < int.MaxValue;
    }

    public Vector2Int CalculatePos(int idx)
    {
        int y = idx / mMapWidth;
        int x = idx - mMapWidth * y;
        return new Vector2Int(x, y);
    }

    public Vector2Int[] PathTo(Vector2Int target)
    {
        Stack<Vector2Int> path = new Stack<Vector2Int>();
        path.Push(target);
        int idx = CalculateIdx(ref target);
        int parentIdx = edgeTo[idx];
        while(parentIdx != mStartIdx)
        {
            path.Push(CalculatePos(parentIdx));
            parentIdx = edgeTo[parentIdx];
        }
        path.Push(mStartPos);

        return path.ToArray();
    }

    /// <summary>
    /// 二维坐标转换下标
    /// </summary>
    /// <param name="cp"></param>
    /// <returns></returns>
    int CalculateIdx(ref Vector2Int cp)
    {
        return cp.y * mMapWidth + cp.x;
    }

    public void Excute(Vector2Int starPos, Vector2Int endPos, CellStatus[,] cells)
    {
        int xLen = cells.GetLength(0);
        int yLen = cells.GetLength(1);
        mMapWidth = xLen;
        mMapHeight = yLen;
        mStartPos = starPos;
        mStartIdx = CalculateIdx(ref starPos);

        int size = xLen * yLen;
        edgeTo = new int[size];
        distTo = new int[size];
        for (int x = 0; x < size; x++)
        {
            distTo[x] = int.MaxValue;
        }
        distTo[mStartIdx] = 0;
        for (int x = 0; x < size; x++)
        {
            edgeTo[x] = -1;
        }
        edgeTo[mStartIdx] = mStartIdx;

        openList = new Queue<Vector2Int>(8);


        openList.Enqueue(starPos);

        while (openList.Count > 0)
        {
            var top = openList.Dequeue();
            Relax(top, ref xLen, ref yLen, cells);
        }

        Debug.Log("构建完毕");
    }


    //  5   6   7
    //  3   P   4
    //  0   1   2
    void Relax(Vector2Int pos, ref int width, ref int height, CellStatus[,] cells)
    {
        //左右八个点
        Vector2Int cp = pos;
        int pIdx = CalculateIdx(ref cp);

        //0
        cp.x = pos.x - 1;
        cp.y = pos.y - 1;
        Relax(pIdx, 14, cp, ref width, ref height, cells);

        //1
        cp.x = pos.x;
        cp.y = pos.y - 1;
        Relax(pIdx, 10, cp, ref width, ref height, cells);

        //2
        cp.x = pos.x + 1;
        cp.y = pos.y - 1;
        Relax(pIdx, 14, cp, ref width, ref height, cells);

        //3
        cp.x = pos.x - 1;
        cp.y = pos.y;
        Relax(pIdx, 10, cp, ref width, ref height, cells);
        //4
        cp.x = pos.x + 1;
        cp.y = pos.y;
        Relax(pIdx, 10, cp, ref width, ref height, cells);

        //5
        cp.x = pos.x - 1;
        cp.y = pos.y + 1;
        Relax(pIdx, 14, cp, ref width, ref height, cells);
        //6
        cp.x = pos.x;
        cp.y = pos.y + 1;
        Relax(pIdx, 10, cp, ref width, ref height, cells);
        //7
        cp.x = pos.x + 1;
        cp.y = pos.y + 1;
        Relax(pIdx, 14, cp, ref width, ref height, cells);
    }

    Queue<Vector2Int> temp = new Queue<Vector2Int>();
    void Relax(int curIdx, int weight, Vector2Int cp, ref int width, ref int height, CellStatus[,] cells)
    {
        if (cp.x >= 0 && cp.x < width && cp.y >= 0 && cp.y < height && cells[cp.x, cp.y] != CellStatus.Obstacle)
        {
            int idx = CalculateIdx(ref cp);
            if (distTo[idx] > distTo[curIdx] + weight)
            {
                //放松边
                distTo[idx] = distTo[curIdx] + weight;
                edgeTo[idx] = curIdx;

                if(openList.Contains(cp))
                {
                    //交换到队尾
                    temp.Clear();
                    while(openList.Count > 0)
                    {
                        var p = openList.Dequeue();
                        if (cp != p)
                        {
                            temp.Enqueue(p);
                        }
                    }
                    while (temp.Count > 0)
                    {
                        var p = temp.Dequeue();
                        openList.Enqueue(p);
                    }

                    openList.Enqueue(cp);
                }
                else
                {
                    //加入队列
                    openList.Enqueue(cp);
                }
            }
        }
    }
}
