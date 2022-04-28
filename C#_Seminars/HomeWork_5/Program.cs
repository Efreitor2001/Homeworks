// Задача 1: Напишите цикл, который принимает на вход два числа (A и B)
// и возводит число A в натуральную степень B.
Console.Write("Input first number: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Input second number: ");
int b = Convert.ToInt32(Console.ReadLine());
int count = 0;
int result = 1;
while (count != b)
{
    result *= a;
    count++;
}
Console.WriteLine(result);

// Задача 2: Напишите программу, которая принимает на вход число
// и выдаёт сумму цифр в числе.
Console.Write("Input Your number: ");
int num = Convert.ToInt32(Console.ReadLine());
int res = 0;
while (num / 10 != 0)
{
    res += num % 10;
    num /= 10;
}
res += num;
Console.WriteLine(res); // Самое универсальное решение этой задачи.

// Задача 3: Напишите программу, которая задаёт массив
// из 8 элементов и выводит их на экран.
int[] CreateArray()
{
    int[] array = new int[8];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(1, 101);
    }
    return array;
}
void PrintArray(int[] a)
{
    Console.Write("[");
    for (int i = 0; i < a.Length - 1; i++)
    {
        Console.Write(a[i] + ", ");
    }
    Console.WriteLine(a[7] + "]");
}
PrintArray(CreateArray());
// Лис Сэнсей, в чём подвох!? \\