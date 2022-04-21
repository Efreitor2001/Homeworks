int c;
/* Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами.
Напишите программу, которая покажет количество чётных чисел в массиве. */

int CountArray(int lengthArray)
{
    int[] a = new int[lengthArray];
    int count = 0;
    for (int i = 0; i < a.Length; i++)
    {
        a[i] = new Random().Next();
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
var length1 = Console.ReadLine();
bool IsNum1 = int.TryParse(length1, out c);
while (IsNum1 == false)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("Error, input correct numner: ");
    Console.ForegroundColor = ConsoleColor.Green;
    length1 = Console.ReadLine();
    IsNum1 = int.TryParse(length1, out c);
}
Console.WriteLine("Count even numbers in array = " + CountArray(Convert.ToInt32(length1)));
Console.WriteLine();

/* Задача 36: Задайте одномерный массив, заполненный случайными числами.
Найдите сумму элементов, стоящих на нечётных позициях. */

int SumArray(int lengthArray)
{
    int[] b = new int[lengthArray];
    int sum = 0;
    for (int index = 0; index < b.Length; index++)
    {
        b[index] = new Random().Next();
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
Console.Write("Input array lenght: ");
var length2 = Console.ReadLine();
bool IsNum2 = int.TryParse(length2, out c);
while (IsNum2 == false)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("Error, input correct numner: ");
    Console.ForegroundColor = ConsoleColor.Green;
    length2 = Console.ReadLine();
    IsNum2 = int.TryParse(length2, out c);
}
Console.WriteLine("Sum elements in odd positions = " + SumArray(Convert.ToInt32(length2)));
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
var length3 = Console.ReadLine();
bool IsNum3 = int.TryParse(length3, out c);
while (IsNum3 == false)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("Error, input correct numner: ");
    Console.ForegroundColor = ConsoleColor.Green;
    length3 = Console.ReadLine();
    IsNum3 = int.TryParse(length3, out c);
}
DiffArray(Convert.ToInt32(length3));
Console.WriteLine();