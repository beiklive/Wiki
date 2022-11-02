---
comments: true
---


## 控制台2048
<img src="img/2048.png" alt="2048"  />

!!! note
    头文件`tabulate/table.hpp`地址：[https://github.com/p-ranav/tabulate](https://github.com/p-ranav/tabulate)

```c title="main.cpp" linenums="1"
#include "tabulate/table.hpp"

#include <unistd.h>
#include <string>
#include <termio.h>
#include <stdlib.h>
using namespace tabulate;

const unsigned char CTRL_KEY = 'q';
const unsigned char LEFT = 'a';
const unsigned char RIGHT = 'd';
const unsigned char DOWN = 's';
const unsigned char UP = 'w';
const int MAXPOINT = 128;

int table1024[4][4] = {0};
int totalscore = 0;

int getch(void)
{
    int ch;
    struct termios tm, tm_old;
    tcgetattr(STDIN_FILENO, &tm);
    tm_old = tm;
    tm.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &tm);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &tm_old);
    return ch;
}

void screenClear()
{
#ifdef __linux__
    std::cout << "\033c";
#else
    system("cls");
#endif
}

std::string tableTransFormat(int a)
{
    return (a == 0 ? " " : std::to_string(a));
}

void tableFlush(int score, int table[][4])
{
    screenClear();
    Table title_score;
    title_score.add_row({"total_score : " + std::to_string(score)});
    title_score[0].format().font_align(FontAlign::center).width(25);

    Table styled_table;
    styled_table.add_row({tableTransFormat(table[0][0]), tableTransFormat(table[0][1]), tableTransFormat(table[0][2]), tableTransFormat(table[0][3])});
    styled_table.add_row({tableTransFormat(table[1][0]), tableTransFormat(table[1][1]), tableTransFormat(table[1][2]), tableTransFormat(table[1][3])});
    styled_table.add_row({tableTransFormat(table[2][0]), tableTransFormat(table[2][1]), tableTransFormat(table[2][2]), tableTransFormat(table[2][3])});
    styled_table.add_row({tableTransFormat(table[3][0]), tableTransFormat(table[3][1]), tableTransFormat(table[3][2]), tableTransFormat(table[3][3])});

    title_score.add_row({styled_table});
    title_score[1].format().font_align(FontAlign::center);
    std::cout << title_score << std::endl;
}

int randomPosGet()
{
    int r = rand() % 4;
    return r;
}

void scoreSet(int var)
{
    if (var <= MAXPOINT && var > 0)
    {
        totalscore += var;
    }
    else
    {
        totalscore = 0;
    }
}

void clearMax(int x, int y, int table[][4])
{
    if (table[x][y] == MAXPOINT)
    {
        table[x][y] = 0;
    }
}

bool elemGen(int table[][4])
{
    int i = randomPosGet(), j = randomPosGet();
    int flag = 0;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (table[i][j] == 0)
            {
                flag = 1;
            }
        }
    }
    if (flag == 0)
    {
        return false;
    }
    while (table[i][j] != 0)
    {
        i = randomPosGet();
        j = randomPosGet();
    }
    table[i][j] = (rand() % 2) * 2 + 2;
    return true;
}

void tableReset(int table[][4])
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            table[i][j] = 0;
        }
    }
    scoreSet(-1);
}

void MoveElemToLeft(int table[][4])
{
    int loopc = 3;
    while (loopc--)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                clearMax(j, i, table);
                if (table[j][i] == 0)
                {
                    table[j][i] = table[j][i + 1];
                    table[j][i + 1] = 0;
                }
                else if (table[j][i] == table[j][i + 1])
                {
                    scoreSet(table[j][i]);
                    table[j][i] += table[j][i + 1];
                    table[j][i + 1] = 0;
                }
            }
        }
    }
}

void MoveElemToRight(int table[][4])
{
    int loopc = 3;
    while (loopc--)
    {
        for (int i = 3; i > 0; i--)
        {
            for (int j = 0; j < 4; j++)
            {
                clearMax(j, i, table);
                if (table[j][i] == 0)
                {
                    table[j][i] = table[j][i - 1];
                    table[j][i - 1] = 0;
                }
                else if (table[j][i] == table[j][i - 1])
                {
                    scoreSet(table[j][i]);
                    table[j][i] += table[j][i - 1];
                    table[j][i - 1] = 0;
                }
            }
        }
    }
}

void MoveElemToUp(int table[][4])
{
    int loopc = 3;
    while (loopc--)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                clearMax(j, i, table);
                if (table[i][j] == 0)
                {
                    table[i][j] = table[i + 1][j];
                    table[i + 1][j] = 0;
                }
                else if (table[i][j] == table[i + 1][j])
                {
                    table[i][j] += table[i + 1][j];
                    table[i + 1][j] = 0;
                    scoreSet(table[i][j]);
                }
            }
        }
    }
}

void MoveElemToDown(int table[][4])
{
    int loopc = 3;
    while (loopc--)
    {
        for (int i = 3; i > 0; i--)
        {
            for (int j = 0; j < 4; j++)
            {
                clearMax(j, i, table);
                if (table[i][j] == 0)
                {
                    table[i][j] = table[i - 1][j];
                    table[i - 1][j] = 0;
                }
                else if (table[i][j] == table[i - 1][j])
                {
                    table[i][j] += table[i - 1][j];
                    table[i - 1][j] = 0;
                    scoreSet(table[i][j]);
                }
            }
        }
    }
}

void oneGapChange(int mode, int table[][4])
{
    switch (mode)
    {
    case 0:
        MoveElemToLeft(table);
        break;
    case 1:
        MoveElemToRight(table);
        break;
    case 2:
        MoveElemToDown(table);
        break;
    case 3:
        MoveElemToUp(table);
        break;
    default:
        break;
    }

    if (elemGen(table))
    {
        elemGen(table);
        tableFlush(totalscore, table);
    }
    else
    {
        tableReset(table);
        tableFlush(totalscore, table);
    }
}

int main()
{
    char a;
    tableFlush(0, table1024);

    while (1)
    {
        switch (a = getch())
        {
        case LEFT:
            oneGapChange(0, table1024);
            std::cout << "LEFT" << std::endl;
            break;
        case RIGHT:
            oneGapChange(1, table1024);
            std::cout << "RIGHT" << std::endl;
            break;
        case DOWN:
            oneGapChange(2, table1024);
            std::cout << "DOWN" << std::endl;
            break;
        case UP:
            oneGapChange(3, table1024);
            std::cout << "UP" << std::endl;
            break;
        case CTRL_KEY:
            std::cout << "exit" << std::endl;
            return 0;
        default:
            tableFlush(totalscore, table1024);
            std::cout << a << std::endl;
            break;
        }
    }
}
```
