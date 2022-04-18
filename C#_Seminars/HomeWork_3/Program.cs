/* Задача 19. Напишите программу, которая принимает на вход пятизначное число
 и проверяет, является ли оно палиндромом. */
/* Console.ForegroundColor = ConsoleColor.Green;
void Pal(string s)
{
    var b = new string(s.Reverse().ToArray());
    if (Convert.ToInt32(s) == Convert.ToInt32(b))
    {
        Console.Write("Number " + s + " is ");
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.WriteLine("a palindrome");
    }
    else
    {
        Console.Write("Number " + s + " is ");
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("NOT a palindrome");
    }
}
Console.Write("Input number: ");
var a = Console.ReadLine();
int c;
void isNum()
{
    bool IsNum = int.TryParse(a, out c);
    while (IsNum == false)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.Write("Error, input correct numner: ");
        Console.ForegroundColor = ConsoleColor.Green;
        a = Console.ReadLine();
        IsNum = int.TryParse(a, out c);
    }
}
isNum();
while (Convert.ToInt32(a) < 10000 || Convert.ToInt32(a) > 99999)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Write("Error, input correct numner: ");
    Console.ForegroundColor = ConsoleColor.Green;
    a = Console.ReadLine();
    isNum();
}
a = Convert.ToString(c);
Pal(a); */

/* Задача 21. Напишите программу, которая принимает на вход координаты двух точек
 и находит расстояние между ними в 3D пространстве. */
Console.ForegroundColor = ConsoleColor.Green;
/*void A(double xA, double yA, double zA)
{
    xA = Convert.ToDouble(Console.Read());
    yA = Convert.ToDouble(Console.Read());
    zA = Convert.ToDouble(Console.Read());
}*/
void DotA(double[] a)
{
    for (int i = 0; i < 3; i++)
    {
        switch (i)
        {
            case 0:
                Console.Write("Input X coordinate for A dot: ");
                a[i] = Convert.ToDouble(Console.ReadLine());
                break;
            case 1:
                Console.Write("Input Y coordinate for A dot: ");
                a[i] = Convert.ToDouble(Console.ReadLine());
                break;
            case 2:
                Console.Write("Input Z coordinate for A dot: ");
                a[i] = Convert.ToDouble(Console.ReadLine());
                break;
        }

    }

}
void DotB(double[] b)
{
    for (int i = 0; i < 3; i++)
    {
        switch (i)
        {
            case 0:
                Console.Write("Input X coordinate for B dot: ");
                b[i] = Convert.ToDouble(Console.ReadLine());
                break;
            case 1:
                Console.Write("Input Y coordinate for B dot: ");
                b[i] = Convert.ToDouble(Console.ReadLine());
                break;
            case 2:
                Console.Write("Input Z coordinate for B dot: ");
                b[i] = Convert.ToDouble(Console.ReadLine());
                break;
        }

    }

}
double[] A = new double[3];
DotA(A);
double[] B = new double[3];
DotB(B);
double dist = Math.Sqrt(Math.Pow((B[0] - A[0]), 2) + Math.Pow((B[1] - A[1]), 2) + Math.Pow((B[2] - A[2]), 2));
Console.WriteLine(Math.Round(dist, 2));