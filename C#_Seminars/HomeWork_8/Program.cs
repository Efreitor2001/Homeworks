// Задача 54: Задайте двумерный массив.
// Напишите программу, которая упорядочит по возрастанию элементы каждой строки двумерного массива.
int[,] CreateArray(int size1, int size2)
{
    int[,] rndArray = new int[size1, size2];
    for (int i = 0; i < size1; i++)
    {
        for (int j = 0; j < size2; j++)
        {
            rndArray[i, j] = new Random().Next(1, 101);
        }
    }
    return rndArray;
}
void ShowOriginArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}
int[,] SortArray(int[,] array)
{
    for (int g = 0; g < array.GetLength(1); g++)
    {
        int x = 0;
        for (int i = 0; i < array.GetLength(0); i++)
        {
            for (int j = 0; j < array.GetLength(1) - 1; j++)
            {
                if (array[x, j] > array[x, j + 1])
                {
                    int temp = array[x, j];
                    array[x, j] = array[x, j + 1];
                    array[x, j + 1] = temp;
                }
            }
            x++;
        }
    }
    return array;
}
void ShowSortArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}
Console.Write("Input strings count: ");
int stringsCount = Convert.ToInt32(Console.ReadLine());
Console.Write("Input columns count: ");
int columnsCount = Convert.ToInt32(Console.ReadLine());
int[,] newArray = CreateArray(stringsCount, columnsCount);
ShowOriginArray(newArray);
Console.WriteLine();
ShowSortArray(SortArray(newArray));

// Задача 56: Задайте прямоугольный двумерный массив.
// Напишите программу, которая будет находить строку с наименьшей суммой элементов.
int[,] CreateArra(int size1, int size2)
{
    int[,] array = new int[size1, size2];
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = new Random().Next(1, 101);
        }
    }
    return array;
}
int[] SumInString(int[,] array)
{
    int[] sum = new int[array.GetLength(0)];
    int x = 0;
    int summ = 0;
    for (int i = 0; i < sum.Length; i++)
    {
        for (int j = 0; j < array.GetLength(0); j++)
        {
            for (int g = 0; g < array.GetLength(1); g++)
            {
                summ += array[x, g];
                sum[i] = summ;
            }
            summ = 0;
        }
        x++;
    }
    return sum;
}
void PrintSum(int[] sum)
{
    for (int i = 0; i < sum.Length; i++)
    {
        Console.Write(sum[i] + " ");
    }
    Console.WriteLine();
}
void PrintArra(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}
int MinSumInString(int[] sum)
{
    int min = sum[0];
    int minIndex = 0;
    for (int i = 0; i < sum.Length; i++)
    {
        if (sum[i] <= min)
        {
            min = sum[i];
            minIndex = i + 1;
        }
    }
    return minIndex;
}
Console.Write("Input sting count: ");
int stringCounts = Convert.ToInt32(Console.ReadLine());
Console.Write("Input columns count: ");
int columnsCounts = Convert.ToInt32(Console.ReadLine());
while (stringCounts == columnsCounts)
{
    Console.WriteLine("Error, the array must be rectangular!");
    Console.Write("Input sting count: ");
    stringCounts = Convert.ToInt32(Console.ReadLine());
    Console.Write("Input columns count: ");
    columnsCounts = Convert.ToInt32(Console.ReadLine());
}
int[,] array = CreateArra(stringCounts, columnsCounts);
PrintArra(array);
Console.WriteLine();
PrintSum(SumInString(array));
Console.WriteLine();
Console.WriteLine($"Minimum amount in line {MinSumInString(SumInString(array))}");

// Задача 62. Заполните спирально массив 4 на 4.
int[,] SpiralArray()
{
    int n = 4;
    int m = 4;
    int[,] array = new int[n, m];
    int row = 0;
    int col = 0;
    int dx = 1;
    int dy = 0;
    int dirChanges = 0;
    int visits = m;
    for (int i = 0; i < array.Length; i++)
    {
        array[row, col] = i + 1;
        if (--visits == 0)
        {
            visits = m * (dirChanges % 2) + n * ((dirChanges + 1) % 2) - (dirChanges / 2 - 1) - 2;
            int temp = dx;
            dx = -dy;
            dy = temp;
            dirChanges++;
        }
        col += dx;
        row += dy;
    }
    return array;
}
void ShowArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}
ShowArray(SpiralArray());