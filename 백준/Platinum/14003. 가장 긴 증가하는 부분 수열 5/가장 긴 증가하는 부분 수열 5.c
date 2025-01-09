#include <stdio.h>

int main(void)
{
	int dp[1000001] = { 0 };
	int A[1000001] = { 0 };
	int n;
	int dp_count[1000001] = { 0 };
	int print_n[1000001] = { 0 };

	dp[0] = -10000000001;
	scanf("%d", &n);
	for (int i = 1;i <= n;i++)
	{
		scanf("%d", &A[i]);
	}

	int idx = 0;
	for (int i = 1;i <= n;i++)
	{
		if (dp[idx] < A[i])
		{
			idx++;
			dp[idx] = A[i];
			dp_count[i] = idx;
		}
		else
		{
			int start = 0;
			int end = idx;
			int ex=end;
			while (start <= end)
			{
				int mid = (start + end) / 2;
				if (dp[mid] < A[i])
				{
					ex = mid;
					start = mid + 1;
				}
				else
				{
					ex = mid - 1;
					end = mid - 1;
				}
			}
			dp[ex + 1] = A[i];
			dp_count[i] = ex + 1;
		}
	}

	int count = idx;
	int count_num;
	for (int i = n;i > 0;i--)
	{
		if (dp_count[i] == count && count == idx)
		{
			print_n[count] = A[i];
			count_num = A[i];
			count--;
		}
		else if (dp_count[i] == count && A[i] < count_num)
		{
			print_n[count] = A[i];
			count_num = A[i];
			count--;
		}
	}
	printf("%d",idx);
	printf("\n");
	for (int i = 1;i <= idx;i++)
		printf("%d ", print_n[i]);
	
	
}