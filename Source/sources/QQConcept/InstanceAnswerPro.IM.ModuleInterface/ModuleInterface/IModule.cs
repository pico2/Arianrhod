namespace InstanceAnswerPro.IM.ModuleInterface
{
    using System;

    public interface IModule
    {
        void Load(object root);
        void Unload();
    }
}

