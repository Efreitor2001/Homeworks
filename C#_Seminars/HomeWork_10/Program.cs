// Задача 1: Задайте массив строк.
// Напишите программу, считает кол-во слов в массиве, начинающихся на гласную букву.
string?[] CreateStringsArray(int size)
{
    string?[] array = new string[size];
    for (int i = 0; i < size; i++)
    {
        Console.Write($"Input {i + 1} word: ");
        array[i] = Console.ReadLine();
    }
    return array;
}
int CheckString(string?[] array)
{
    string? check = string.Empty;
    int count = 0;
    string ch = "аеёиоуыэюяaeiouy";
    for (int i = 0; i < array.Length; i++)
    {
        check = array[i];
        for (int j = 0; j < ch.Length; j++)
        {
            if (check[0] == ch[j])
            {
                count++;
            }
        }
    }
    return count;
}
Console.Write("Input words count: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(CheckString(CreateStringsArray(size)));

// Задача 2: Задайте массив строк.
// Напишите программу, которая генерирует новый массив, объединяя элементы исходного массива попарно.
string?[] CreateArray(int size)
{
    string?[] array = new string[size];
    for (int i = 0; i < size; i++)
    {
        Console.Write($"Input {i + 1} word: ");
        array[i] = Console.ReadLine();
    }
    return array;
}
string?[] UnityArray(string?[] array)
{
    int size = array.Length / 2;
    string?[] unitArr = new string[size];
    for (int i = 0, j = 0; i < array.Length - 1; i += 2, j++)
    {
        unitArr[j] = array[i] + array[i + 1];
    }
    return unitArr;
}
void ShowArray(string?[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}
Console.Write("Input words count: ");
int size1 = Convert.ToInt32(Console.ReadLine());
while (size1 % 2 != 0)
{
    Console.Write("Error! Input even number: ");
    size1 = Convert.ToInt32(Console.ReadLine());
}
ShowArray(UnityArray(CreateArray(size1)));