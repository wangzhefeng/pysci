
Decorate Model
======================


装饰模式的类图
-----------------



- Component 是一个抽象类, 代表具有某种功能(function)的组件

    - ComponentImplA 是 Component 的具体的实现子类

    - ComponentImplB 是 Component 的具体的实现子类

    - Decorator 是 Component 的装饰器

        - decorated 是 Decorator 里的 Component 对象

        - addBehavior 是装饰器为被装饰对象添加额外功能或行为的函数

        - DecoratorImplA 是具体的装饰器实现子类
        
        - DecoratorImplB 是具体的装饰器实现子类
