/* Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами.
Напишите программу, которая покажет количество чётных чисел в массиве. */

int CountArray(int lengthArray, int minRandom, int maxRandom)
{
    int[] a = new int[lengthArray];
    int count = 0;
    for (int i = 0; i < a.Length; i++)
    {
        a[i] = new Random().Next(minRandom, maxRandom);
        Console.Write(a[i] + " ");
        if (a[i] % 2 == 0)
        {
            count++;
        }
    }
    Console.WriteLine();
    return count;
}
Console.WriteLine("Task #1");
Console.Write("Input array lenght: ");
int length1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min value for random: ");
int min1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max value for random: ");
int max1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Count even numbers in array = " + CountArray(length1, min1, ++max1));
Console.WriteLine();

/* Задача 36: Задайте одномерный массив, заполненный случайными числами.
Найдите сумму элементов, стоящих на нечётных позициях. */

int SumArray(int lengthArray, int minRandom, int maxRandom)
{
    int[] b = new int[lengthArray];
    int sum = 0;
    for (int index = 0; index < b.Length; index++)
    {
        b[index] = new Random().Next(minRandom, maxRandom);
        Console.Write(b[index] + " ");
        if (index % 2 == 0) // Если 0 индекс это 1 позиция, то так, если имеется ввиду чётность индекса,
        {                   // то index % 2 != 0
            sum += b[index];
        }
    }
    Console.WriteLine();
    return sum;
}
Console.WriteLine("Task #2");
Console.Write("Input array lenght: ");
int length2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Input min value for random: ");
int min2 = Convert.ToInt32(Console.ReadLine());
Console.Write("Input max value for random: ");
int max2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Sum elements in odd positions = " + SumArray(length2, min2, ++max2));
Console.WriteLine();

/* Задача 38: Задайте массив вещественных чисел.
Найдите разницу между максимальным и минимальным элементов массива. */

void DiffArray(int lengthArray)
{
    double[] c = new double[lengthArray];
    double max = 0;
    double min = 1;
    for (int ind = 0; ind < c.Length; ind++)
    {
        c[ind] = new Random().NextDouble();
        Console.Write(Math.Round(c[ind], 2) + " ");
        if (c[ind] > max)
        {
            max = c[ind];
        }
    }
    min = max;
    for (int ind = 0; ind < c.Length; ind++)
    {
        if (c[ind] < min)
        {
            min = c[ind];
        }
    }
    Console.WriteLine();
    Console.WriteLine("Max = " + Math.Round(max, 2));
    Console.WriteLine("Min = " + Math.Round(min, 2));
    Console.WriteLine("Difference between Max and Min = " + Math.Round((max - min), 2));
}
Console.WriteLine("Task #3");
Console.Write("Input array lenght: ");
int length3 = Convert.ToInt32(Console.ReadLine());
DiffArray(length3);
Console.WriteLine();