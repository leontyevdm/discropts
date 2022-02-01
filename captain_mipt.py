import numpy as np
import scipy.optimize as spo
import random
import sys
import time

def read_data():
    with open('dataset_495145_8.txt') as input:
        sys.stdin = input
        n, p, k, M = map(int, sys.stdin.readline().split())
        x = np.ndarray((n, 2))
        money = np.ndarray(n)
        for i in range(n):
            row = list(map(float, sys.stdin.readline().split()))
            x[i] = [row[0], row[1]]
            money[i] = row[2]

    return n, p, k, M, x, money
'''
def check_alco(end, k, money, solution, M):
    sum = 0
    for i in range(end, max(end - k, 0)):
        sum += money[solution[i]]
    if sum > M:
        return False
    return True
def NN(n, x, starting_point=0):
    st = np.zeros(n, dtype=bool)
    ans = list([0] * n)
    cur = starting_point
    st[cur] = True
    ans[0] = starting_point
    for j in range(1, n):
        dists = np.linalg.norm(x[cur] - x, axis=1)
        dists[st] = np.inf
        sort = dists.argsort()
        check = False
        counter = 0

        while not check:
            cur_min_index = sort[counter]
            check = check_alco(j, k, money, ans, M)
            counter += 1
        if cur_min_index >= n:
            return np.flip(np.arange(n))
        st[cur_min_index] = True
        cur = cur_min_index
        ans[j] = cur_min_index
    return ans

def dist(p1, p2):
    return np.linalg.norm(p1 - p2)

def reconnect_2(solution, i, j):
    solution[i:j] = solution[i:j][::-1]

def local_search(x, solution):
    global start_time
    n = len(solution)
    while time.time() - start_time < 300:
        is_changed = False
        for i in range(1, n):
            for j in range(i + 1, n):
                e1p1 = x[solution[i - 1]]
                e1p2 = x[solution[i]]
                e2p1 = x[solution[j - 1]]
                e2p2 = x[solution[j]]

                if dist(e1p1, e1p2) + dist(e2p1, e2p2) > dist(e1p1, e2p1) + dist(e1p2, e2p2):
                    is_changed = True
                    reconnect_2(solution, i, j)
        if not is_changed:
            return

def skip_wasteful_islands(ans, p, x, money):
    new_ans = list([ans[0]])
    for i in range(1, len(ans) - 1):
        if - p * dist(x[new_ans[-1]], x[ans[i + 1]]) < money[ans[i]] - p * (dist(x[new_ans[-1]], x[ans[i]]) + dist(x[ans[i]], x[ans[i + 1]])):
            new_ans.append(ans[i])
    new_ans.append(ans[0])
    return new_ans

start_time = time.time()
n, p, k, M, x, money = read_data()

ans = NN(n, x)
local_search(x, ans)
ans.append(ans[0])

for _ in range(50):
    ans = skip_wasteful_islands(ans, p, x, money)

local_search(x, ans)


for i in range(len(ans)):
        print(ans[i] + 1, end=' ')


with open('output.txt', mode='w') as output: 
    ssss = sys.stdout
    sys.stdout = output
    for i in range(len(ans)):
        print(ans[i] + 1, end=' ')

    sys.stdout = ssss
'''




n, p, k, M, x, money = read_data()
S = '1 800 335 817 173 385 724 537 226 610 470 141 669 162 395 371 230 359 487 938 451 842 121 759 38 312 399 196 14 361 444 110 303 699 425 676 414 432 115 656 891 596 175 829 428 159 339 164 741 731 206 733 7 575 283 559 207 821 10 543 810 514 72 855 394 420 895 965 266 878 860 755 466 368 712 138 105 892 391 488 97 184 979 392 542 928 298 504 99 480 921 329 708 3 398 237 671 703 13 163 302 944 124 62 930 305 169 4 150 88 572 549 199 893 160 589 483 221 565 737 397 452 951 235 587 321 811 627 357 507 566 222 30 202 797 429 875 293 76 316 5 702 805 204 911 809 864 188 945 28 820 898 412 515 861 120 841 962 833 149 167 819 301 865 152 649 290 793 791 948 867 186 151 153 41 550 402 396 353 135 80 297 126 502 161 529 93 413 901 889 365 818 434 86 916 828 57 877 682 738 780 309 822 485 678 274 862 753 133 687 458 130 374 868 613 884 112 563 798 845 431 705 430 354 386 709 852 581 666 742 765 812 978 632 949 189 532 594 486 306 323 90 332 582 578 904 748 256 970 356 813 598 463 92 46 564 925 136 280 422 762 638 933 122 719 236 823 941 257 484 100 725 212 761 44 82 595 633 794 874 21 477 896 843 754 409 856 517 446 757 445 406 690 363 355 461 927 612 421 109 560 223 597 684 348 211 625 704 950 749 871 639 416 954 369 658 539 132 535 912 260 214 917 379 907 264 953 768 590 148 307 849 85 63 108 609 322 468 959 934 344 940 261 58 689 902 660 801 328 971 825 721 830 334 129 919 201 806 509 289 571 418 324 415 932 623 497 673 607 866 519 707 288 16 555 453 592 882 720 552 752 373 360 74 176 785 103 158 295 435 185 326 652 246 972 243 352 686 772 94 799 311 576 267 31 29 876 282 111 455 956 292 528 294 64 964 410 668 393 615 494 456 635 653 438 25 522 255 404 531 645 383 384 551 618 835 789 436 499 787 277 790 745 538 200 54 48 501 247 193 275 79 245 569 117 47 119 498 511 59 442 620 314 662 854 659 37 675 573 561 977 648 440 98 345 766 974 580 78 908 143 228 24 736 880 179 194 469 181 838 493 533 18 249 19 128 782 50 495 443 83 774 688 284 39 106 351 647 318 272 744 644 914 746 715 890 888 611 118 180 513 481 769 603 471 541 628 626 367 23 9 910 55 646 781 654 616 198 310 508 973 857 123 232 665 655 370 491 96 681 53 837 259 271 146 464 905 225 606 101 591 942 319 2 401 714 967 554 447 579 238 667 454 608 52 803 71 771 377 70 832 980 614 706 969 946 570 234 460 313 500 642 113 808 732 380 27 756 827 116 171 846 457 482 850 479 553 826 139 848 473 630 640 546 926 816 178 197 568 773 521 574 599 218 220 107 788 400 696 154 6 217 140 216 320 840 664 629 804 650 524 419 65 643 8 381 641 844 287 747 510 349 600 366 583 505 739 77 624 955 340 557 693 387 465 450 936 700 899 920 411 792 795 210 526 784 815 924 710 343 43 42 558 534 474 718 192 84 26 492 378 853 286 957 317 375 338 713 963 548 847 467 894 937 779 567 17 556 155 268 701 265 490 858 91 631 496 166 263 327 634 269 403 680 870 372 300 530 604 209 872 241 36 783 81 636 233 663 873 915 777 619 291 102 976 637 476 601 503 929 735 145 740 478 506 764 931 315 516 711 12 776 203 760 15 961 168 131 87 279 960 426 831 909 248 75 968 51 836 730 734 518 205 585 45 545 900 165 683 190 775 325 174 834 966 975 61 427 376 472 134 939 346 441 95 763 489 657 923 364 73 786 691 672 172 408 142 913 887 750 11 231 729 125 242 227 68 258 906 281 331 593 651 462 147 527 407 56 104 342 213 439 336 20 433 605 127 588 347 935 69 886 621 362 253 814 333 952 692 251 562 182 958 252 685 674 602 824 137 661 859 778 802 839 544 727 584 716 390 278 195 89 34 423 726 717 304 698 863 254 869 32 622 382 219 389 743 459 918 512 250 448 577 405 262 144 677 239 240 697 807 449 49 722 586 285 157 796 170 67 276 341 547 208 770 191 224 22 885 330 947 728 723 694 66 437 270 922 177 540 60 187 879 358 388 670 424 229 35 114 758 617 903 883 751 767 417 536 350 475 215 296 183 851 679 308 520 244 881 33 523 695 40 897 299 273 156 525 337 943 1'

l = S.split()
for i in range(len(l)):
  l[i] = int(l[i])
l.pop()
for i in range(len(l)):
    print(l[i], money[l[i] - 1])
    sum = money[l[i] - 1] + money[l[i + 1] - 1] + money[l[i + 2] - 1] + money[l[i + 3] - 1]+ money[l[i+4] - 1]
    if sum > 7654:
      maxim = np.argmax([money[l[i] - 1] + money[l[i + 1] - 1] + money[l[i + 2] - 1] + money[l[i + 3] - 1]+ money[l[i+4] - 1]])
      print(maxim)
