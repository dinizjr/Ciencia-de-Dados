BEGIN TRANSACTION QUICKDBD

CREATE TABLE [ClinicaMedica].[Consulta] (
    [ConsutaID] int  NOT NULL ,
    [Data] date  NOT NULL ,
    [MedicoID] int  NOT NULL ,
    [PacienteID] int  NOT NULL ,
    CONSTRAINT [PK_Consulta] PRIMARY KEY CLUSTERED (
	[ConsutaID] ASC
	)
)

CREATE TABLE [ClinicaMedica].[Medico] (
    [MedicoID] int  NOT NULL ,
    [EspecialidadeID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    CONSTRAINT [PK_Medico] PRIMARY KEY CLUSTERED (
        [MedicoID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Especialidade] (
    [EspecialidadeID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    CONSTRAINT [PK_Especialidade] PRIMARY KEY CLUSTERED (
        [EspecialidadeID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Tipo_Exame] (
    [Tipo_ExameID] int  NOT NULL ,
    [Custo] numeric(11,2)  NOT NULL ,
    CONSTRAINT [PK_Tipo_Exame] PRIMARY KEY CLUSTERED (
        [Tipo_ExameID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Pacientes] (
    [PacienteID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    [Telefone] varchar(200)  NOT NULL ,
    [PlanoID] int  NOT NULL ,
    CONSTRAINT [PK_Pacientes] PRIMARY KEY CLUSTERED (
        [PacienteID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Fornecedores] (
    [FornecedoresID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    CONSTRAINT [PK_Fornecedores] PRIMARY KEY CLUSTERED (
        [FornecedoresID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Exames] (
    [ExameID] int  NOT NULL ,
    [PacienteID] int  NOT NULL ,
    [MedicoID] int,
    [Tipo_ExameID] int  NOT NULL ,
    [Data_Exame] date  NOT NULL ,
    CONSTRAINT [PK_Exames] PRIMARY KEY CLUSTERED (
        [ExameID] ASC
    ),
	CONSTRAINT FK_Paciente_Exame FOREIGN KEY (PacienteID) REFERENCES [ClinicaMedica].[Pacientes](PacienteID),
	CONSTRAINT FK_MedicoExame FOREIGN KEY (MedicoID) REFERENCES [ClinicaMedica].[Medico](MedicoID),
	CONSTRAINT FK_Tipo_Exame FOREIGN KEY (Tipo_ExameID) REFERENCES [ClinicaMedica].[Tipo_Exame](Tipo_ExameID),
)

CREATE TABLE [ClinicaMedica].[Suprimentos] (
    [SuprimentosID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    [FornecedoresID] int  NOT NULL ,
    CONSTRAINT [PK_Suprimentos] PRIMARY KEY CLUSTERED (
        [SuprimentosID] ASC
    ),
    CONSTRAINT [UK_Suprimentos_Nome] UNIQUE (
        [Nome]
    )
)



CREATE TABLE [ClinicaMedica].[Planos_Saude] (
    [PlanoID] int  NOT NULL ,
    [Nome] varchar(200)  NOT NULL ,
    CONSTRAINT [PK_Planos_Saude] PRIMARY KEY CLUSTERED (
        [PlanoID] ASC
    )
)

CREATE TABLE [ClinicaMedica].[Cobertura_Exames] (
    [Tipo_ExameID] int  NOT NULL ,
    [PlanoID] int  NOT NULL ,
    CONSTRAINT [PK_Cobertura_Exames] PRIMARY KEY CLUSTERED (
        [Tipo_ExameID] ASC,[PlanoID] ASC
    )
)

ALTER TABLE [ClinicaMedica].[Consulta] WITH CHECK ADD CONSTRAINT [FK_Consulta_MedicoID] FOREIGN KEY([MedicoID])
REFERENCES [ClinicaMedica].[Medico] ([MedicoID])

ALTER TABLE [ClinicaMedica].[Consulta] CHECK CONSTRAINT [FK_Consulta_MedicoID]

ALTER TABLE [ClinicaMedica].[Consulta] WITH CHECK ADD CONSTRAINT [FK_Consulta_PacienteID] FOREIGN KEY([PacienteID])
REFERENCES [ClinicaMedica].[Pacientes] ([PacienteID])

ALTER TABLE [ClinicaMedica].[Consulta] CHECK CONSTRAINT [FK_Consulta_PacienteID]

ALTER TABLE [ClinicaMedica].[Medico] WITH CHECK ADD CONSTRAINT [FK_Medico_EspecialidadeID] FOREIGN KEY([EspecialidadeID])
REFERENCES [ClinicaMedica].[Especialidade] ([EspecialidadeID])

ALTER TABLE [ClinicaMedica].[Medico] CHECK CONSTRAINT [FK_Medico_EspecialidadeID]

ALTER TABLE [ClinicaMedica].[Suprimentos] WITH CHECK ADD CONSTRAINT [FK_Suprimentos_FornecedoresID] FOREIGN KEY([FornecedoresID])
REFERENCES [ClinicaMedica].[Fornecedores] ([FornecedoresID])

ALTER TABLE [ClinicaMedica].[Suprimentos] CHECK CONSTRAINT [FK_Suprimentos_FornecedoresID]

ALTER TABLE [ClinicaMedica].[Pacientes] WITH CHECK ADD CONSTRAINT [FK_Pacientes_PlanoID] FOREIGN KEY([PlanoID])
REFERENCES [ClinicaMedica].[Planos_Saude] ([PlanoID])

ALTER TABLE [ClinicaMedica].[Pacientes] CHECK CONSTRAINT [FK_Pacientes_PlanoID]

ALTER TABLE [ClinicaMedica].[Cobertura_Exames] WITH CHECK
ADD CONSTRAINT FK_Plano_Cobertura_Exames FOREIGN KEY (PlanoID) REFERENCES [ClinicaMedica].[Planos_Saude](PlanoID)

ALTER TABLE [ClinicaMedica].[Cobertura_Exames] WITH CHECK
ADD CONSTRAINT FK_Tipo_Exame_Cobertura_Exames FOREIGN KEY (Tipo_ExameID) REFERENCES [ClinicaMedica].[Tipo_Exame](Tipo_ExameID)

CREATE TABLE [ClinicaMedica].[Cobertura_Especialidade] (
	PlanoID int not null,
	EspecialidadeID int not null,
	CONSTRAINT PK_Cobertura_Especialidade_ID PRIMARY KEY CLUSTERED ([PlanoID] ASC , [EspecialidadeID] ASC),
	CONSTRAINT FK_Plano_Cobertura FOREIGN KEY (PlanoID) REFERENCES [ClinicaMedica].[Planos_Saude](PlanoID),
	CONSTRAINT FK_Especialidade_Cobertura FOREIGN KEY (EspecialidadeID) REFERENCES [ClinicaMedica].[Especialidade](EspecialidadeID)
)

CREATE TABLE [ClinicaMedica].[Suprimentos_Tipo] (
	Tipo_ExameID int not null,
	SuprimentosID int not null,
	CONSTRAINT PK_Suprimentos_Tipo_ID PRIMARY KEY CLUSTERED ([Tipo_ExameID] ASC , [SuprimentosID] ASC),
	CONSTRAINT FK_Exame_SuprimentosTipo FOREIGN KEY (Tipo_ExameID) REFERENCES [ClinicaMedica].[Tipo_Exame](Tipo_ExameID),
	CONSTRAINT FK_Suprimentos_SuprimentosTipo FOREIGN KEY (SuprimentosID) REFERENCES [ClinicaMedica].[Suprimentos](SuprimentosID)
)

CREATE TABLE [ClinicaMedica].[Fornecedores_Tipo] (
	Tipo_ExameID int not null,
	FornecedoresID int not null,
	CONSTRAINT PK_Fornecedores_Tipo_ID PRIMARY KEY CLUSTERED ([Tipo_ExameID] ASC , [FornecedoresID] ASC),
	CONSTRAINT FK_Exame_FornecedoresTipo FOREIGN KEY (Tipo_ExameID) REFERENCES [ClinicaMedica].[Tipo_Exame](Tipo_ExameID),
	CONSTRAINT FK_Fornecedores_FornecedoresTipo FOREIGN KEY (FornecedoresID) REFERENCES [ClinicaMedica].[Fornecedores](FornecedoresID)
)

COMMIT TRANSACTION QUICKDBD

