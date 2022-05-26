// Задача 66: Задайте значения M и N.
// Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
int Sum(int m, int n)
{
    if (n < m)
        return 1;
    return m + Sum(m + 1, n);
}
Console.Write("Input M num: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Input N num: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(Sum(m, n) - 1);

// Задача 67: Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.
int SumDigit(int num)
{
    if (num == 0)
        return 0;
    return num % 10 + SumDigit(num / 10);
}
Console.Write("Input Your number: ");
int num = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(SumDigit(num));