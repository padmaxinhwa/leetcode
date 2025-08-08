
# LeetCode

- 직접 풀이 후 해설 / 시간복잡도 정리
- 이틀에 3문제 목표
- [Top Interview 150](https://leetcode.com/list/xi4ci4ig/) 병행
- Python, Java 등 언어별로 풀이 저장 가능하도록 디렉토리 구성 (`/python/`, `/java/` 등)

<br>

## 📌 주제별 기본 문제

| Topic | No | Title | Difficulty | Remarks |
|-------|----|-------|------------|---------|
| Big-O| [#704](https://leetcode.com/problems/binary-search/) | Binary Search | Easy | Binary search 기본 |
| | [#35](https://leetcode.com/problems/search-insert-position/) | Search Insert Position | Easy | 이진탐색 응용 |
| | [#977](https://leetcode.com/problems/squares-of-a-sorted-array/) | Squares of a Sorted Array | Easy | 투 포인터 연습 |
| 자료구조 | [#20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | Easy | 스택 기본 |
| | [#155](https://leetcode.com/problems/min-stack/) | Min Stack | Medium | 스택 구조 설계 |
| | [#347](https://leetcode.com/problems/top-k-frequent-elements/) | Top K Frequent Elements | Medium | Heap & HashMap |
| 그래프 | [#200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | Medium | DFS/BFS 기본 |
| | [#417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic Water Flow | Medium | DFS + 조건 파악 |
| | [#684](https://leetcode.com/problems/redundant-connection/) | Redundant Connection | Medium | Union Find |
| 정수론 | [#231](https://leetcode.com/problems/power-of-two/) | Power of Two | Easy | 비트 연산 가능 |
| | [#326](https://leetcode.com/problems/power-of-three/) | Power of Three | Easy | 수학적 사고 |
| | [#204](https://leetcode.com/problems/count-primes/) | Count Primes | Medium | 소수 에라토스테네스 체 |
|  조합 / 백트래킹 | [#78](https://leetcode.com/problems/subsets/) | Subsets | Medium | 백트래킹 기본 |
| | [#46](https://leetcode.com/problems/permutations/) | Permutations | Medium | 순열 구현 |
| | [#39](https://leetcode.com/problems/combination-sum/) | Combination Sum | Medium | 중복 조합 |
| 동적 계획법 (DP) | [#70](https://leetcode.com/problems/climbing-stairs/) | Climbing Stairs | Easy | 피보나치 유사 |
| | [#198](https://leetcode.com/problems/house-robber/) | House Robber | Medium | 선택-비선택 DP |
| | [#300](https://leetcode.com/problems/longest-increasing-subsequence/) | Longest Increasing Subsequence | Medium | DP + 이진 탐색 가능 |
| 기하 | [#1232](https://leetcode.com/problems/check-if-it-is-a-straight-line/) | Check If It Is a Straight Line | Easy | 직선 기울기 계산 |
| | [#149](https://leetcode.com/problems/max-points-on-a-line/) | Max Points on a Line | Hard | 기울기 처리 주의 |
| | [#587](https://leetcode.com/problems/erect-the-fence/) | Erect the Fence | Hard | Convex Hull |
| 정규표현식 & 패턴 매칭 | [#8](https://leetcode.com/problems/string-to-integer-atoi/) | String to Integer (atoi) | Medium | 구현 복잡 |
| | [#10](https://leetcode.com/problems/regular-expression-matching/) | Regular Expression Matching | Hard | DP로 풀이 |
| | [#65](https://leetcode.com/problems/valid-number/) | Valid Number | Hard | 구현 + 유효성 검사 |
| 슬라이딩 윈도우 | [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | Medium | 슬라이딩 윈도우 |
| | [#567](https://leetcode.com/problems/permutation-in-string/) | Permutation in String | Medium | 윈도우 내 비교 |
| | [#76](https://leetcode.com/problems/minimum-window-substring/) | Minimum Window Substring | Hard | 두 포인터 & 카운터 |

<br>

## 📌 면접에서 자주 출제되는 문제

| Topic | No | Title | Difficulty | Remarks |
|-------|----|-------|------------|---------|
| Sliding Window | [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | Medium |
| | [#76](https://leetcode.com/problems/minimum-window-substring/) | Minimum Window Substring | Hard |
| | [#438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Find All Anagrams in a String | Medium |
| Two Pointers | [#15](https://leetcode.com/problems/3sum/) | 3Sum | Medium |
| | [#11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water | Medium |
| | [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Remove Duplicates from Sorted Array | Easy |
| Binary Search| [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Search in Rotated Sorted Array | Medium |
| | [#153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Find Minimum in Rotated Sorted Array | Medium |
| | [#875](https://leetcode.com/problems/koko-eating-bananas/) | Koko Eating Bananas | Medium |
| Greedy | [#55](https://leetcode.com/problems/jump-game/) | Jump Game | Medium |
| | [#134](https://leetcode.com/problems/gas-station/) | Gas Station | Medium |
| | [#253](https://leetcode.com/problems/meeting-rooms-ii/) | Meeting Rooms II | Medium |
| Backtracking / DFS | [#46](https://leetcode.com/problems/permutations/) | Permutations | Medium |
| | [#79](https://leetcode.com/problems/word-search/) | Word Search | Medium |
| | [#22](https://leetcode.com/problems/generate-parentheses/) | Generate Parentheses | Medium |
| Heap / Priority Queue | [#621](https://leetcode.com/problems/task-scheduler/) | Task Scheduler | Medium |
| | [#295](https://leetcode.com/problems/find-median-from-data-stream/) | Find Median from Data Stream | Hard |
| | [#23](https://leetcode.com/problems/merge-k-sorted-lists/) | Merge k Sorted Lists | Hard |
| Trie | [#208](https://leetcode.com/problems/implement-trie-prefix-tree/) | Implement Trie (Prefix Tree) | Medium |
| | [#211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Design Add and Search Words Data Structure | Medium |
| | [#212](https://leetcode.com/problems/word-search-ii/) | Word Search II | Hard |
| Union-Find | [#547](https://leetcode.com/problems/number-of-provinces/) | Number of Provinces | Medium |
| | [#684](https://leetcode.com/problems/redundant-connection/) | Redundant Connection | Medium |
| | [#1319](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Number of Operations to Make Network Connected | Medium |
| Topological Sort | [#207](https://leetcode.com/problems/course-schedule/) | Course Schedule | Medium |
| | [#210](https://leetcode.com/problems/course-schedule-ii/) | Course Schedule II | Medium |
| | [#269](https://leetcode.com/problems/alien-dictionary/) | Alien Dictionary | Hard |
| Dynamic Programming | [#198](https://leetcode.com/problems/house-robber/) | House Robber | Medium |
| | [#62](https://leetcode.com/problems/unique-paths/) | Unique Paths | Medium |
| | [#1143](https://leetcode.com/problems/longest-common-subsequence/) | Longest Common Subsequence | Medium |
| | [#5](https://leetcode.com/problems/longest-palindromic-substring/) | Longest Palindromic Substring | Medium |


