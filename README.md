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


### AndroidX升级之路

#### 升级门槛

1. AndroidStudio3.2+
2. gradle 3.2.0+
3. targetSdkVersion 28+

升级过程

1. 修改配置文件

    修改gradle.properties
    android.useAndroidX=true 表示启用 androidx
    android.enableJetifier=true 表示将依赖包也迁移到androidx 。如果取值为false,表示不迁移依赖包到androidx，但在使用依赖包中的内容时可能会出现问题，如果项目中没有使用任何三方依赖，可以设置为false。
    
    使用android.enableJetifier=true将项目中使用的第三方库也迁移到 Androidx，迁移后还需要 Flie -> Invalidate Caches /Restart 一下。

1. 在AS中执行Refactor->Migrate to AndroidX。

填大坑

1. import包很多需要手动修改，可以选择全局替换，建议整理一个替换文档
2. ButterKnife需要升级到兼容androidx的版本
3. Glide需要升级到4.8版本及以上，手动把annotationProcessor引用改成androidx包名
4. 去除attr.xml重名问题，androidx不允许自定义属性和系统属性同名


