class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int b = 0, a = 0, l = 0, o = 0, n = 0;
        for (auto i : text) {
            if (i == 'a') a++;
            else if (i == 'b') b++;
            else if (i == 'l') l++;
            else if (i == 'o') o++;
            else if (i == 'n') n++;
        }

        int x = min(a, min(b, n));
        int y = min(l, o) / 2;
        return min(x, y);
    }
};