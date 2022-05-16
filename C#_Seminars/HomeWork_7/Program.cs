// Задача 47. Задайте двумерный массив размером m×n,
// заполненный случайными вещественными числами.
double[,] CreateArray(int size1, int size2)
{
    double[,] randomArray = new double[size1, size2];
    for (int i = 0; i < randomArray.GetLength(0); i++)
    {
        for (int j = 0; j < randomArray.GetLength(1); j++)
        {
            randomArray[i, j] = new Random().NextDouble();
        }
    }
    return randomArray;
}
void PrintArray(double[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            Console.Write(Math.Round(arr[i, j], 2) + " ");
        }
        Console.WriteLine();
    }
}
Console.Write($"Iput m number: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write($"Iput n number: ");
int n = Convert.ToInt32(Console.ReadLine());
PrintArray(CreateArray(m, n));

// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
// и возвращает значение этого элемента или же указание, что такого элемента нет.
int[,] RandomArray()
{
    int[,] rndmArray = new int[new Random().Next(5, 11), new Random().Next(5, 11)];
    for (int i = 0; i < rndmArray.GetLength(0); i++)
    {
        for (int j = 0; j < rndmArray.GetLength(1); j++)
        {
            rndmArray[i, j] = new Random().Next(1, 100);
        }
    }
    return rndmArray;
}
void ShowElement(int[,] array, int pos1, int pos2)
{
    int a = array.GetLength(0);
    int b = array.GetLength(1);
    if (pos1 <= a && pos2 <= b && pos1 > 0 && pos2 > 0)
    {
        Console.WriteLine($"Element in position {pos1} {pos2} = {array[pos1 - 1, pos2 - 1]}");
    }
    else
    {
        Console.WriteLine($"Not found element in position {pos1} {pos2}");
    }
}
Console.Write("Input first position: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.Write("Input second position: ");
int y = Convert.ToInt32(Console.ReadLine());
ShowElement(RandomArray(), x, y);

// Задача 52. Задайте двумерный массив из целых чисел.
// Найдите среднее арифметическое элементов в каждом столбце.
int[,] CreateArr()
{
    int[,] arra = new int[new Random().Next(5, 11), new Random().Next(5, 11)];
    for (int i = 0; i < arra.GetLength(0); i++)
    {
        for (int j = 0; j < arra.GetLength(1); j++)
        {
            arra[i, j] = new Random().Next(1, 101);
            Console.Write(arra[i, j] + " ");
        }
        Console.WriteLine();
    }
    return arra;
}
double[] MOC(int[,] ar)
{
    double sum = 0;
    int size = ar.GetLength(0);
    double[] average = new double[ar.GetLength(1)];
    int x = 0;
    for (int i = 0; i < average.Length; i++)
    {
        for (int j = 0; j < ar.GetLength(0); j++)
        {
            sum += ar[j, x];
            for (int g = 0; g < ar.GetLength(1); g++)
            {
                average[i] = sum / size;
            }
        }
        x++;
        sum = 0;
    }
    return average;
}
void PrintMOC(double[] a)
{
    for (int i = 0; i < a.Length; i++)
    {
        Console.Write(Math.Round(a[i], 2) + " ");
    }
    Console.WriteLine();
}
PrintMOC(MOC(CreateArr()));