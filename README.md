# NEU-CodeAudit
一个简单的支持c语言的代码编辑器和代码检测器
# 运行
直接运行 Controller/loginRegiser/login.py 即可，没有注册账号请先注册。
# 环境要求
1.LeanCloud云服务器账户
Data/leancloud.py 文件下的
```python
appId = 'Your appID'
appKey = 'Your appKey'
masterkey = "Your masterkey"
```
请替换为自己LeanCloud账户的appId，appKey，masterkey。

2. Flawfinder
Flawfinder是一个静态代码分析工具，用于检测C和C++程序中的安全漏洞。它由David A. Wheeler开发，旨在帮助开发人员在编写代码时发现常见的安全问题。Flawfinder的工作原理是通过对源代码进行扫描和分析来查找潜在的安全漏洞。它使用一个基于规则的系统，其中包含了数百个已知的漏洞模式。这些规则涵盖了各种安全问题，包括缓冲区溢出、格式化字符串漏洞、代码注入等。
Flawfinder在Pyhon3.x中集成有库，因此直接在对应环境下输入命令即可：
```
pip3 install flawfinder
```
使用如下命令即可对test.c文件使用Flawfinder静态扫描：
```
flawfinder test.c
```

3. CppChecker
Cppcheck是一个开源的静态代码分析工具，用于检测C和C++程序中的错误、不一致性和潜在的安全问题。它可以帮助开发人员在编写代码时发现常见的编程错误，并提供有关如何修复这些问题的建议。Cppcheck使用静态分析技术来检查源代码，而无需实际运行程序。它通过解析源代码，构建抽象语法树，并应用一系列规则来查找潜在问题。这些规则涵盖了各种编程错误，包括空指针解引用、内存泄漏、类型不匹配、未初始化变量等。
Cppcheck在Pyhon3.x中没有对应的库，作为一个第三方工具，需要通过官网下载：
```
http://cppcheck.net/
```
下载完成后,添加对应文件到系统变量PATH中。
使用如下命令即可对test.c文件路径使用Cppchecker静态扫描：
```
cppcheck --enable=all --std=c11 --verbose D:\work1\c_test_file\test.c
```
此命令表示在启用所有规则的情况下，使用C11标准对位于指定路径的test.c文件进行详细的静态代码分析，并生成相应的报告：
cppcheck: 这是运行Cppcheck的命令。
--enable=all: 这个选项告诉Cppcheck启用所有可用的检查规则。它将对源代码文件执行所有可能的检查，包括错误、警告和其他问题。
--std=c11: 这个选项指定了源代码文件所使用的C语言标准。在这种情况下，它指定使用C11标准。Cppcheck会根据指定的语言标准进行相应的静态代码分析。
--verbose: 这个选项启用详细模式，将输出更详细的信息。它会显示Cppcheck的执行过程中的详细信息，包括正在检查的文件、检查的规则和可能的问题。
D:\work1\c_test_file\test.c: 这是要进行静态代码分析的源代码文件的路径。在这个例子中，test.c是位于D:\work1\c_test_file\目录下的文件，Cppcheck将对其进行分析并生成相应的报告。

4. Dr.memory
Dr. Memory是一个开源的动态内存错误检测工具，专门用于C和C++程序。它可以帮助开发人员发现和调试内存相关的错误，如内存泄漏、访问无效内存、使用未初始化的内存等。Dr. Memory使用动态二进制插桩技术，将目标程序加载到内存中，并对其进行运行时分析。它能够检测到许多内存相关的问题，并生成详细的报告，指出问题发生的位置、类型和可能的原因。
Dr. Memory在Pyhon3.x中没有对应的库，作为一个第三方工具，需要通过官网下载：
```
https://drmemory.org/
```
下载完成后,添加对应bin和bin64文件路径到系统变量PATH中。

使用如下命令即可对test.c文件路径使用Dr. Memory内存扫描：
```
drmemory.exe D:\work1\c_test_file\test.exe
```

5. LLVM && Clang工具链
LLVM和Clang是两个紧密相关的开源工具，构成了一个现代化、高效的编译器工具链。它们的设计目标是提供高度可优化的代码生成、快速的编译过程、灵活的架构以及广泛的支持多种编程语言。LLVM是一个编译器基础设施，是一个用于优化和生成中间代码（IR）的开源项目。LLVM以中间表示（IR）作为中间语言，提供了许多优化器和工具，使得编译器可以在IR层面进行优化。这种设计使得LLVM可以支持多种编程语言，并且可以用于不同的平台和架构。Clang是LLVM项目中的一个子项目，是一个C、C++、Objective-C和Objective-C++编译器前端。它采用LLVM作为后端，将C/C++/Objective-C代码转换为LLVM的中间表示（IR），然后由LLVM后端生成机器码。
LLVM和Clang工具链提供了强大而灵活的编译器基础设施，支持多种编程语言，并为开发者提供了快速编译和高度优化的代码生成。
LLVM && Clang工具链在Pyhon3.x中没有对应的库，但是提供了Clang库，在文件树和语法树的构造中我们使用了Clang库。但是Pyhon3.x中的Clang库功能比较有限，作为一个第三方工具，需要通过官网下载：
```
https://github.com/llvm
```
安装完成后，在对应的文件目录显示如下：

这里建议将bin和libexec文件夹均添加到系统变量PATH中。
LLVM和Clang工具链在bin文件夹下集成了大量的工具。下面对我们项目中使用的工具进行简介。

5.1 clang
Clang是LLVM项目中的一个子项目，它是一个C、C++、Objective-C和Objective-C++编译器前端。作为LLVM工具链的一部分，Clang负责将C、C++、Objective-C和Objective-C++等高级编程语言的源代码转换为LLVM的中间表示（IR）。
使用如下命令使用Clang编译器以"gcc"驱动模式编译D:/work1/c_test_file/test.c文件，并启用所有警告信息和调试符号，生成一个名为test.exe的可执行文件，并将其输出到D:/work1/c_test_file/目录下：
```
clang --driver-mode=gcc -Wall -g3 -o D:/work1/c_test_file/test.exe D:/work1/c_test_file/test.c
```
clang: 这是要执行的编译器，即Clang编译器。
--driver-mode=gcc: 这个选项指定了Clang的驱动模式为"gcc"。这个选项通常用于确保Clang在行为上与GCC（GNU Compiler Collection）兼容。
-Wall: 这个选项启用了所有的警告信息。编译器将会输出关于代码中潜在问题的警告信息。
-g3: 这个选项启用了用于调试的符号信息，并指定了调试级别为3。这将使得生成的可执行文件包含更多的调试信息，有助于在调试过程中定位问题。
-o D:/work1/c_test_file/test.exe: 这个选项指定了生成的可执行文件的输出路径和名称。在这个例子中，可执行文件将会被输出到D:/work1/c_test_file/目录下，并命名为test.exe。
D:/work1/c_test_file/test.c: 这是要进行编译的C语言源代码文件的路径。在这个例子中，test.c是位于D:/work1/c_test_file/目录下的文件，它将会被编译成可执行文件。

5.2 clang-tidy
clang-tidy是一个用于C++代码的静态代码分析工具，是Clang工具集的一部分。它基于LLVM和Clang，旨在帮助开发人员发现并修复代码中的一些常见问题和潜在错误，以提高代码质量、可读性和安全性。
使用如下命令使用clang-tidy工具对位于D:/work1/c_test_file/test.c路径下的C语言源代码文件进行静态代码分析，应用所有可用的检查规则，并在分析过程中包含所有的头文件，并使用C11标准来解析源代码。
```
clang-tidy.exe -checks=*, -header-filter=.*, -extra-arg=-std=c11 D:/work1/c_test_file/test.c
```
clang-tidy.exe: 这是要执行的clang-tidy工具的可执行文件。
-checks=*: 这个选项指定要应用的检查规则。*表示应用所有可用的检查规则，即对源代码执行所有可能的检查。
-header-filter=.*: 这个选项指定要分析的头文件。.*表示所有的头文件都会被分析。
-extra-arg=-std=c11: 这个选项向编译器传递额外的参数。在这个例子中，它指定编译器使用C11标准来解析源代码。
D:/work1/c_test_file/test.c: 这是要进行静态代码分析的C语言源代码文件的路径。在这个例子中，test.c是位于D:/work1/c_test_file/目录下的文件，clang-tidy将对其进行分析。

5.3 clang-format
clang-format是一个开源的代码格式化工具，属于Clang工具集的一部分。它旨在自动化对C、C++、Objective-C和JavaScript等编程语言的代码进行格式化，以保持一致的代码风格和可读性。clang-format根据一组预定义的或自定义的代码样式规则来格式化源代码文件。这些规则涵盖了各种代码格式化方面，例如缩进、空格、换行、对齐等。通过应用这些规则，clang-format可以将代码自动调整为符合统一的代码风格，并帮助开发团队遵循一致的编码规范。
使用如下命令使用clang-format工具对C语言源代码文件D:/work1/c_test_file/test.c进行代码格式化，并将格式化后的结果直接写回到源代码文件中。
```
clang-format.exe -style=LLVM -i D:/work1/c_test_file/test.c
```
clang-format.exe: 这是要执行的clang-format工具的可执行文件。
-style=LLVM: 这个选项指定了使用的代码样式规则。在这个例子中，使用了LLVM样式规则，它是clang-format预定义的一种代码样式，通常用于符合LLVM项目的代码风格。
-i: 这个选项表示对源代码文件进行原地修改，即将格式化后的结果直接写回到源文件中，而不是生成一个格式化后的副本。
D:/work1/c_test_file/test.c: 这是要进行代码格式化的C语言源代码文件的路径。在这个例子中，test.c是位于D:/work1/c_test_file/目录下的文件，clang-format将对其进行代码格式化，并将格式化后的结果保存回原始文件。

5.4 clang-check
类似于Clang-Tidy,clang-check是LLVM/Clang工具集中的一个实用工具，它用于执行Clang静态分析器（Clang Static Analyzer）来检测C、C++和Objective-C源代码中的静态错误和潜在问题。但是通常情况下，clang-check更加灵活，可以自定义命令以达到用户期望的效果。
使用如下命令使用clang-check工具对位于D:/work1/c_test_file/test.c路径下的C语言源代码文件进行静态代码分析，并启用额外的编译参数-Wall、-Wextra、-Werror和-pedantic，从而输出所有警告信息并将警告视为严重问题。
```
clang-check.exe -extra-arg=-Wall -extra-arg=-Wextra -extra-arg=-Werror -extra-arg=-pedantic D:/work1/c_test_file/test.c --
```
clang-check.exe: 这是要执行的clang-check工具的可执行文件。
-extra-arg=-Wall: 这个选项指定了额外的编译参数-Wall，它是GCC和Clang等编译器中的一个标志，用于启用所有的警告信息。这将使得静态分析器检查代码时输出所有的警告。
-extra-arg=-Wextra: 这个选项指定了额外的编译参数-Wextra，它也是GCC和Clang中的标志，用于启用额外的警告选项，提供更详细的警告信息。
-extra-arg=-Werror: 这个选项指定了额外的编译参数-Werror，它是GCC和Clang中的标志，用于将所有警告视为错误。这将导致静态分析器将所有的警告视为严重问题，并中止分析过程。
-extra-arg=-pedantic: 这个选项指定了额外的编译参数-pedantic，它是GCC和Clang中的标志，用于启用严格的ANSI/ISO标准的警告信息。这将导致静态分析器检查代码时输出符合ANSI/ISO标准的严格警告信息。
D:/work1/c_test_file/test.c: 这是要进行静态代码分析的C语言源代码文件的路径。在这个例子中，test.c是位于D:/work1/c_test_file/目录下的文件，clang-check将对其进行分析。

5.5 scan-build
scan-build是一个开源的静态代码分析工具，旨在帮助开发人员在C、C++和Objective-C项目中发现代码中的潜在问题和错误。它是Clang工具集中的一个工具，利用了Clang静态分析器（Clang Static Analyzer）来进行静态代码分析。
和clang-tidy和clang-check不同的是，scan-build可以生成一份友好的面向User的报告。另外，网络上在Windows操作系统上scan-build命令的使用几乎没有现成的资料，加上此部分需要的系统环境较复杂，因此这个部分的开发使用比较困难。
Windows用户必须安装Perl才能使用scan-build。要从任意位置调用 scan-build，请将包含 scan-build.bat 的文件夹的路径添加到 PATH 环境变量中。
进入PERL官网下载：
```
https://www.perl.org/
```
下载完成后,添加对应bin文件路径到系统变量PATH中：

使用如下命令使用scan-build工具对C语言源代码文件D:/work1/c_test_file/test.c进行静态代码分析。
```
scan-build --use-cc=X:/llvm/libexec/ccc-analyzer --use-analyzer=X:/llvm/bin/clang.exe clang D:/work1/c_test_file/test.c
```
scan-build: 这是要执行的scan-build工具的可执行文件。
--use-cc=X:/llvm/libexec/ccc-analyzer: 这个选项指定了ccc-analyzer的路径，它是Clang的C语言前端编译器，用于生成分析所需的中间表示（IR）。
--use-analyzer=X:/llvm/bin/clang.exe: 这个选项指定了clang.exe的路径，它是Clang的C/C++/Objective-C前端编译器，用于执行实际的代码分析。
clang: 这是要分析的编译器。在这个例子中，clang是用于执行实际的代码分析。
D:/work1/c_test_file/test.c: 这是要进行静态代码分析的C语言源代码文件的路径。在这个例子中，test.c是位于D:/work1/c_test_file/目录下的文件，scan-build将对其进行静态代码分析。

5.6 llvm-cov
llvm-cov是LLVM/Clang工具集中的一个工具，用于代码覆盖率分析。它能够帮助开发人员了解在运行测试套件或应用程序时，源代码中哪些部分被执行了，哪些部分未被执行，从而评估代码覆盖率。
llvm-cov命令的执行比较复杂。首先，使用如下命令使用clang编译器对C语言源代码文件D:/work1/c_test_file/test.c进行编译，并生成一个可执行文件。同时，它添加了一些选项来启用代码覆盖率收集功能，用于生成代码覆盖率报告。
```
clang -fprofile-instr-generate=test.profraw -fcoverage-mapping  D:/work1/c_test_file/test.c -o D:/work1/c_test_file/test.exe
```
其次，使用llvm-profdata工具将两个代码覆盖率数据文件合并成一个。
```
llvm-profdata merge -o D:/work1/c_test_file/test.profdata D:/work1/c_test_file/test.profraw
```
最后，使用 llvm-cov 工具对位于 D:\work1\c_test_file\test.exe 的可执行文件进行代码覆盖率报告。
```
llvm-cov report D:\work1\c_test_file\test.exe -instr-profile=D:\work1\c_test_file\test.profdata
```

6 其他工具:GCC
GCC（GNU Compiler Collection）是一套开源的编程语言编译器，由GNU计划开发和维护。它是一个强大而广泛使用的编译器集合，支持多种编程语言，包括C、C++、Objective-C、Fortran、Ada和其他语言。
使用如下命令使用gcc编译器编译test.c文件。
```
gcc -o D:\work1\c_test_file\test.exe D:\work1\c_test_file\test.c
```

# 以上环境部署完成后，即可开始运行程序啦，环境配置过程较为冗杂，耐心~~~~
