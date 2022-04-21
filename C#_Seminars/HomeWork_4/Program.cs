/* Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами.
Напишите программу, которая покажет количество чётных чисел в массиве. */
int CountArray()
{
    int[] a = new int[10];
    int count = 0;
    for (int i = 0; i < a.Length; i++)
    {
        a[i] = new Random().Next(100, 1000);
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
Console.WriteLine("Count even numbers in array = " + CountArray());
Console.WriteLine();

/* Задача 36: Задайте одномерный массив, заполненный случайными числами.
Найдите сумму элементов, стоящих на нечётных позициях. */

int SumArray()
{
    int[] b = new int[10];
    int sum = 0;
    for (int index = 0; index < b.Length; index++)
    {
        b[index] = new Random().Next(1, 11);
        Console.Write(b[index] + " ");
        if (index % 2 != 0)
        {
            sum += b[index];
        }
    }
    Console.WriteLine();
    return sum;
}
Console.WriteLine("Task #2");
Console.WriteLine("Sum elements in odd positions = " + SumArray());
Console.WriteLine();

/* Задача 38: Задайте массив вещественных чисел.
Найдите разницу между максимальным и минимальным элементов массива. */

void DiffArray()
{
    double[] c = new double[10];
    double max = 0;
    double min = 1;
    for (int ind = 0; ind < c.Length; ind++)
    {
        c[ind] = new Random().Next(1, 100);
        Console.Write(c[ind] + " ");
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
    Console.WriteLine("Max = " + max);
    Console.WriteLine("Min = " + min);
    Console.WriteLine("Difference between Max and Min = " + (max - min));
}
Console.WriteLine("Task #3");
DiffArray();
Console.WriteLine();