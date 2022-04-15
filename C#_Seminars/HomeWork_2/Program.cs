/* Задача 10: Напишите программу, которая принимает на вход трёхзначное число
и на выходе показывает вторую цифру этого числа. */
/*
Console.ForegroundColor = ConsoleColor.Green;
void ShowSecondNum(int num)
{
   int num1 = num / 10;
   int num2 = num1 % 10;
   Console.ForegroundColor = ConsoleColor.Blue;
   Console.WriteLine("The second digit in " + num + " is " + num2 + ".");
}
Console.Write("Input number: ");
var number = Console.ReadLine();
int secondNum = 0;
bool isNum()
{
    bool IsNum = int.TryParse(number, out secondNum);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct day: ");
        Console.ForegroundColor = ConsoleColor.Green;
        number = Console.ReadLine();
        IsNum = int.TryParse(number, out secondNum);
    }
    return true;
}
while (secondNum < 100 || secondNum > 999)
{
   Console.ForegroundColor = ConsoleColor.Red;
   Console.Write("Error, input correct number: ");
   Console.ForegroundColor = ConsoleColor.Green;
   number = Console.ReadLine();
   isNum();
}
ShowSecondNum(secondNum);
*/
/* Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным. */
/*
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
var num = Console.ReadLine();
int day;
bool isNum()
{
    bool IsNum = int.TryParse(num, out day);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct day: ");
        Console.ForegroundColor = ConsoleColor.Green;
        num = Console.ReadLine();
        IsNum = int.TryParse(num, out day);
    }
    return true;
}
isNum();
while (day < 1 || day > 7)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("Error!!! Week has only 7 days!");
    Console.ForegroundColor = ConsoleColor.Green;
    Console.Write("Please input correct day: ");
    num = Console.ReadLine();
    isNum();
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
*/