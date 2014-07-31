namespace InstanceAnswerPro.IM.ModuleInterface
{
    using System;

    public class ModuleInformationAttribute : Attribute
    {
        private string _identifier;

        public ModuleInformationAttribute(string identifier)
        {
            this._identifier = identifier;
        }

        public string Identifier
        {
            get
            {
                return this._identifier;
            }
        }
    }
}

