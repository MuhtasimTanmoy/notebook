# Meteor

        // keeps session for encryption
        
        migrator.registerMigration("sessions") { (db) in
            try db.create(table: "sessions", body: { (table) in
                table.column("account",  .text).collate(.localizedCaseInsensitiveCompare)
                table.column("name",  .blob).collate(.localizedCaseInsensitiveCompare)
                table.column("device_id",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("key",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
            })
        }
        
        // Prekeys
        
        migrator.registerMigration("prekeys") { (db) in
            try db.create(table: "prekeys", body: { (table) in
                table.column("account",  .text).collate(.localizedCaseInsensitiveCompare)
                table.column("id",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("key",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
            })
        }
        
        
        migrator.registerMigration("signed_prekeys") { (db) in
            try db.create(table: "signed_prekeys", body: { (table) in
                table.column("account",  .text).collate(.localizedCaseInsensitiveCompare)
                table.column("id",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("key",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
            })
        }
        
        
        migrator.registerMigration("identities") { (db) in
            try db.create(table: "identities", body: { (table) in
                table.column("account",  .text).collate(.localizedCaseInsensitiveCompare)
                table.column("name",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("ownkey", .boolean)
                table.column("fingerprint",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("certificate",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("trust",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
                table.column("active",  .boolean)
                table.column("last_activation",  .datetime).notNull()
                table.column("key",  .text).notNull().collate(.localizedCaseInsensitiveCompare)
            })
        }
