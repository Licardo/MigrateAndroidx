# MigrateAndroidx

android项目在迁移androidx的过程中会涉及到很多类文件的修改，比如依赖、文件导入的包等问题。

有一部分工作Android Studio编译器会帮我们自动处理，还有很多工作需要开发者手动修改，Migrate Androidx项目就是为了解决手动修改工作的痛点应运而生。

### 使用方法

1. gradle.properties文件增加两个配置项 

```groovy
android.useAndroidX = true
android.enableJetifier = true
```

2. 选择Android Studio的Migrate AndroidX 选项

``` mermaid
graph LR
A(Refactor) --> B(Migrate to AndroidX)
B --> C(Backup project as a Zip file)
C --> D(Migrate)

```

3. 把MigrateAndroidX项目克隆到要迁移的项目根目录

```python
python migrate.py
```



