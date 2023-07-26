using Microsoft.EntityFrameworkCore;

namespace AccountManagementService
{
    public class AccountManagementContext : DbContext
    {
        public AccountManagementContext(DbContextOptions<AccountManagementContext> options)
            : base(options)
        {
        }

        public DbSet<Account> Accounts { get; set; }
    }
}
