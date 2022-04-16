/* Задача 10: Напишите программу, которая принимает на вход трёхзначное число
и на выходе показывает вторую цифру этого числа. */

Console.ForegroundColor = ConsoleColor.Gray;
Console.WriteLine("Task number 1");
Console.ForegroundColor = ConsoleColor.Green;
Console.Write("Input number: ");
var number = Console.ReadLine();
int secondNum;
bool isNum1()
{
    bool IsNum = int.TryParse(number, out secondNum);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct number: ");
        Console.ForegroundColor = ConsoleColor.Green;
        number = Console.ReadLine();
        IsNum = int.TryParse(number, out secondNum);
    }
    return true;
}
isNum1();
void ShowSecondNum(int num2)
{
    num2 /= 10;
    num2 %= 10;
    if (num2 < 0) num2 *= (-1);
    Console.ForegroundColor = ConsoleColor.Blue;
    Console.WriteLine("The second digit in " + number + " is " + num2 + ".");
}
while ((Convert.ToInt32(number) < 100 || Convert.ToInt32(number) > 999) && (Convert.ToInt32(number) > (-100) || Convert.ToInt32(number) < (-999)))
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("Error, input correct number: ");
    Console.ForegroundColor = ConsoleColor.Green;
    number = Console.ReadLine();
    isNum1();
}
ShowSecondNum(secondNum);
Console.WriteLine();

// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

Console.ForegroundColor = ConsoleColor.Gray;
Console.WriteLine("Task number 2");
Console.ForegroundColor = ConsoleColor.Green;
Console.Write("Input number: ");
var enter = Console.ReadLine();
int num;
bool isNum2()
{
    bool IsNum = int.TryParse(enter, out num);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct number: ");
        Console.ForegroundColor = ConsoleColor.Green;
        enter = Console.ReadLine();
        IsNum = int.TryParse(enter, out num);
    }
    return true;
}
isNum2();
void ThirdNum(int digit)
{
    while (digit > 999 || digit < (-999))
    {
        digit /= 10;
    }
    digit %= 100;
    digit %= 10;
    if (digit < 0) digit *= (-1);
    Console.ForegroundColor = ConsoleColor.Blue;
    Console.WriteLine("The third digit in " + enter + " is " + digit + ".");
}
if (num < 100 && num > (-100))
{
    Console.WriteLine("Your number don't have third digit!");
}
else
{
    ThirdNum(num);
}
Console.WriteLine();
/* Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным. */

Console.ForegroundColor = ConsoleColor.Gray;
Console.WriteLine("Task number 3");
Console.ForegroundColor = ConsoleColor.Green;
bool Weekend(int dayNum)
{
    switch (dayNum)
    {
        case 6:
            return true;
        case 7:
            return true;
        default:
            return false;

    }
}
Console.Write("Input day: ");
var num3 = Console.ReadLine();
int day;
bool isNum3()
{
    bool IsNum = int.TryParse(num3, out day);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct day: ");
        Console.ForegroundColor = ConsoleColor.Green;
        num3 = Console.ReadLine();
        IsNum = int.TryParse(num3, out day);
    }
    return true;
}
isNum3();
while (day < 1 || day > 7)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("Error!!! Week has only 7 days!");
    Console.ForegroundColor = ConsoleColor.Green;
    Console.Write("Please input correct day: ");
    num3 = Console.ReadLine();
    isNum3();
}
if (Weekend(day) == true)
{
    Console.ForegroundColor = ConsoleColor.Blue;
    Console.WriteLine("Wow! Today is the weekend!");
}
else
{
    Console.ForegroundColor = ConsoleColor.Yellow;
    Console.WriteLine("Today is not a weekend! =(");
}