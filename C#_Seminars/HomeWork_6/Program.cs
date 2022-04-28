// Задача 41: Пользователь вводит с клавиатуры M чисел.
// Посчитайте, сколько чисел больше 0 ввёл пользователь.
int CountGreaterZero(int[] a)
{
    int count = 0;
    for (int i = 0; i < a.Length; i++)
    {
        if (a[i] > 0) count++;
    }
    return count;
}
int[] CreateArray(int num)
{
    int[] array = new int[num];
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"Input {i + 1} number: ");
        array[i] = Convert.ToInt32(Console.ReadLine());
    }
    return array;
}
Console.Write("Input count numbers: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"Count numbers greater than zero = {CountGreaterZero(CreateArray(n))}");

// Задача 42: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
string TBNS(int num)
{
    string result = String.Empty;
    while (num > 0)
    {
        result += Convert.ToString((num % 2));
        num /= 2;
    }
    result = new string (result.Reverse().ToArray());
    return  result;
}
Console.Write("Input number to convert in TBNS: ");
int num2 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"Your number in the binary numeral system = {TBNS(num2)}");

// Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых,
// заданных уравнениями y = k1 * x + b1, y = k2 * x + b2;
// значения b1, k1, b2 и k2 задаются пользователем.
double[] StraightA(double b1, double k1)
{
    double[] straight1 = new double[2];
    straight1[0] = b1;
    straight1[1] = k1;
    return straight1;
}
double[] StraightB(double b2, double k2)
{
    double[] straight2 = new double[2];
    straight2[0] = b2;
    straight2[1] = k2;
    return straight2;
}
double[] IntersectionPoint(double[] a, double[] b)
{
    double x = 0;
    double[] xp = new double[4];
    double y;
    xp[0] = a[0];
    xp[1] = a[1];
    xp[2] = b[0];
    xp[3] = b[1];
    x += (xp[3] - xp[1]) / (xp[0] - xp[2]);
    y = a[0] * ((xp[3] - xp[1]) / (xp[0] - xp[2])) + xp[1];
    double[] result = new double[2];
    result[0] = x;
    result[1] = y;
    return result;
}
void ShowResult(double[] res)
{
    for (int i = 0; i < res.Length; i++)
    {
        if (i == 0) Console.Write($"x = {Math.Round(res[i], 2)}; ");
        else Console.Write($"y = {Math.Round(res[i], 2)}");
    }
}
Console.Write("Input k1: ");
double k1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input b1: ");
double b1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input k2: ");
double k2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Input b2: ");
double b2 = Convert.ToDouble(Console.ReadLine());
ShowResult(IntersectionPoint(StraightA(k1, b1), StraightB(k2, b2)));
Console.WriteLine();