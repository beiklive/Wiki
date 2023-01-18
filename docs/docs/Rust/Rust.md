---
comments: true
---

## 模块导入
!!! note "main.rs"
    导入模块使用的是模块的文件名
    ```rust
    mod sub_main;
    use sub_main::say;
    use sub_main::say::sub_main;

    fn main() {
        sub_main::say::sub_main(1);
        say::sub_main(2);
        sub_main(3);
    }
    ```
!!! note "sub_main.rs"
    只有赋予了`pub`公开权限的方法才能在外部被调用，不添加`pub`关键字，默认为私有
    ```rust
    pub mod say {
        fn add(a: i32, b: i32) -> i32{
            return a + b;
        }

        pub fn sub_main(index: i32) {
            println!("number: {}", add(index, 1));
        }
    }
    ```