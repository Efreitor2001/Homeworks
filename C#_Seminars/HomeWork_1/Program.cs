﻿Console.ForegroundColor = ConsoleColor.Green; // Самая важная строчка, без неё ничего не заработает!
// Задача 1: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
/* while(true)
{
    double max;
    double f_num;
    double s_num;
    Console.Write("Enter the first number: ");
    var num1 = Console.ReadLine();
    bool is_num = double.TryParse(num1, out f_num);
    while(is_num == false)
    if (is_num == false)
    {
        Console.Write("Error, please enter correct the first number: ");
        num1 = Console.ReadLine();
        is_num = double.TryParse(num1, out f_num);
    }
    Console.Write("Enter the second number: ");
    var num2 = Console.ReadLine();
    bool is_num2 = double.TryParse(num2, out s_num);
    while(is_num2 == false)
    if (is_num2 == false)
    {
        Console.Write("Error, please enter correct the second number: ");
        num2 = Console.ReadLine();
        is_num2 = double.TryParse(num2, out s_num);
    }
    if(f_num == s_num)
    {
        Console.WriteLine("Your numbers are equal");
    }
    else
    {
        if(f_num > s_num)
        {
            max = f_num;
        }
        else
        {
            max = s_num; 
        }

        Console.WriteLine("The larger number is " + max);
    }
} */

// Задача 2: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
while(true)
{
    double max;
    double f_num;
    double s_num;
    double t_num;
    Console.Write("Enter the first number: ");
    var num1 = Console.ReadLine();
    bool is_num = double.TryParse(num1, out f_num);
    while(is_num == false)
    if (is_num == false)
    {
        Console.Write("Error, please enter correct the first number: ");
        num1 = Console.ReadLine();
        is_num = double.TryParse(num1, out f_num);
    }
    Console.Write("Enter the second number: ");
    var num2 = Console.ReadLine();
    bool is_num2 = double.TryParse(num2, out s_num);
    while(is_num2 == false)
    if (is_num2 == false)
    {
        Console.Write("Error, please enter correct the second number: ");
        num2 = Console.ReadLine();
        is_num2 = double.TryParse(num2, out s_num);
    }
    Console.Write("Enter the third number: ");
    var num3 = Console.ReadLine();
    bool is_num3 = double.TryParse(num3, out t_num);
    while(is_num3 == false)
    if (is_num3 == false)
    {
        Console.Write("Error, please enter correct the third number: ");
        num2 = Console.ReadLine();
        is_num2 = double.TryParse(num3, out t_num);
    }
    if((f_num == s_num) & (s_num == t_num) & (t_num == f_num))
    {
        Console.WriteLine("Your numbers are equal");
    }
    else
    {
        if(f_num > s_num & f_num > t_num)
        {
            max = f_num;
        }
        else
        {
            if(s_num > f_num & s_num > t_num)
            {
                max = s_num;
            }
            else
            {
                max = t_num;
            }
        }

        Console.WriteLine("The larger number is " + max);
    }
}