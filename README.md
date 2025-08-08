
# LeetCode

- 주석 자세히 / 시간복잡도 정리
- 이틀에 3문제 목표 🚀
- [Top Interview 150](https://leetcode.com/list/xi4ci4ig/) 병행
- Python, Java 등 언어별로 풀이 저장 가능하도록 디렉토리 구성 (`/python/`, `/java/` 등)

<br>

<details>
  <summary> Python vs Java</summary>
  
#### ✅ Python vs Java: 코딩테스트 언어 비교
| 항목               | 🐍 Python                                          | ☕ Java                                                     |
| ---------------- | -------------------------------------------------- | ---------------------------------------------------------- |
| **작성 속도**        | **매우 빠름** – 문법이 간결하고 타입 선언 불필요                     | 느림 – 타입 선언, 클래스 구조 필요                                      |
| **자료구조 사용**      | 내장 자료형 (`dict`, `set`, `heapq`, `collections`) 풍부  | `HashMap`, `PriorityQueue`, `Deque` 등 명시적 import와 타입 지정 필요 |
| **문법 직관성**       | **높음** – `for x in list`, `if x in set`처럼 자연스럽다    | 상대적으로 복잡 – 반복문, 조건문 등이 장황함                                 |
| **입출력 처리**       | 기본 `input()`은 느림 (⇒ `sys.stdin.readline()` 필요)     | 기본 `Scanner`는 느림 (⇒ `BufferedReader` 권장)                   |
| **정확한 시간 제어**    | 느릴 수 있음 – 대형 입력에서는 TLE가 발생하기 쉬움                    | 상대적으로 빠름 – JVM 오버헤드는 있으나 전반적으로 안정적                         |
| **라이브러리/알고리즘**   | `math`, `itertools`, `bisect`, `heapq` 등 유용한 도구 다수 | 알고리즘은 직접 구현하는 경우가 많음                                       |
| **언어 제한** (플랫폼별) | 일부 기업에서는 **Java/C++만 허용**                          | 거의 모든 플랫폼에서 사용 가능                                          |
| **정수 범위**        | 자동으로 BigInteger 처리 (Overflow 없음)                   | `int` vs `long` 구분 필요, overflow 주의                         |
| **디버깅/IDE 지원**   | 간단한 디버깅은 쉬우나 대규모 개발에는 IDE 의존도 낮음                   | IDE 지원(예: IntelliJ) 매우 우수 – 디버깅과 리팩토링에 강함                  |
| **코드 스타일**       | 짧고 간결한 구현 → 시간 절약                                  | 명시적이고 안정적인 구현 → 실수 적음                                      |

#### ✅ Python vs Java: 코딩테스트 언어 비교
| 상황                                            | 추천 언어             |
| --------------------------------------------- | ----------------- |
| 시간이 **매우 촉박**한 1\~2문제 테스트 (예: 삼성, 네이버 1차 테스트) | **Python**        |
| 대형 기업에서의 **대규모 입력 처리** (예: 카카오, NHN)          | **Java**          |
| 주 언어가 **Java이며 기본기에 강한 편**                    | **Java 유지 권장**    |
| 파이썬이 익숙하고 **코딩에 자신 있음**                       | **Python 적극 추천**  |
| C++에 가까운 **최적화, 정교한 메모리 컨트롤**이 필요             | 둘 다 아님 (→ C++ 추천) |

#### ✅ 추천 전략
- 시간이 부족하거나 아이디어가 핵심인 문제는 Python으로 빠르게 작성
- 시간 제한이 빡빡하거나 대용량 입출력/정밀도 이슈가 있으면 Java 활용
- 이미 Java에 익숙하시다면, Python은 세컨드 언어로 풀이 연습용으로만 활용하고, 실전은 Java로 유지해도 좋습니다.

</details>



<details>
  <summary> 풀이 예제 </summary>
  
#### ✅ 문제: 3. Longest Substring Without Repeating Characters (Medium)
- Given a string s, find the length of the longest substring without repeating characters.

#### ✅ 핵심 아이디어 (Sliding Window)
- **Two pointers (left, right)**를 사용해 슬라이딩 윈도우 범위를 유지
- 중복 문자가 없을 때까지 윈도우 확장, 중복이 생기면 왼쪽 포인터를 줄이며 제거
- 각 단계마다 최대 길이를 업데이트

#### ✅ Python 풀이 (with full English comments)

    def lengthOfLongestSubstring(s: str) -> int:
        # Dictionary to store the last seen index of each character
        last_seen = {}

    # Initialize two pointers for the sliding window
    left = 0  # Left boundary of the current window
    max_length = 0  # Maximum length of substring without repeating characters

    # Iterate over each character in the string using the right pointer
    for right, char in enumerate(s):
        # If the character is already in the window (and its index >= left),
        # move the left pointer to the right of the previous occurrence
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1  # shrink the window from the left

        # Update the character's last seen index
        last_seen[char] = right

        # Calculate the current window length and update max_length if needed
        current_window_length = right - left + 1
        max_length = max(max_length, current_window_length)

    return max_length

#### ✅ Java 풀이 (with full English comments)
    import java.util.HashMap;
    
    public class Solution {
        public int lengthOfLongestSubstring(String s) {
            // Map to store the last seen index of each character
            HashMap<Character, Integer> lastSeen = new HashMap<>();

        int left = 0; // Left boundary of the sliding window
        int maxLength = 0; // Maximum length of non-repeating substring

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // If the character was seen and is within the current window
            if (lastSeen.containsKey(currentChar) && lastSeen.get(currentChar) >= left) {
                // Move the left pointer to the right of the last seen position
                left = lastSeen.get(currentChar) + 1;
            }

            // Update the last seen position of the current character
            lastSeen.put(currentChar, right);

            // Calculate window length and update maxLength
            int currentWindowLength = right - left + 1;
            maxLength = Math.max(maxLength, currentWindowLength);
        }

        return maxLength;
      }
    }



</details>

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


