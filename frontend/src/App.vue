<template>
  <div class="flex h-screen overflow-hidden">
    <!-- Sidebar -->
    <aside class="w-64 flex-shrink-0 glass border-r border-white/5 hidden md:flex flex-col">
      <div class="h-16 flex items-center px-6">
        <h1 class="text-2xl font-bold text-gradient tracking-tight">dotG</h1>
      </div>
      
      <nav class="flex-1 px-4 py-6 space-y-2">
        <router-link to="/" class="nav-link" active-class="active">
          <i data-feather="grid" class="w-5 h-5 mr-3"></i> Dashboard
        </router-link>
        <router-link to="/okr" class="nav-link" active-class="active">
          <i data-feather="target" class="w-5 h-5 mr-3"></i> OKRs
        </router-link>
        <router-link to="/feedback" class="nav-link" active-class="active">
          <i data-feather="message-square" class="w-5 h-5 mr-3"></i> Feedback
        </router-link>
        <router-link to="/1on1" class="nav-link" active-class="active">
          <i data-feather="users" class="w-5 h-5 mr-3"></i> 1-on-1s
        </router-link>
      </nav>

      <div class="p-4 border-t border-white/5">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 flex items-center justify-center font-bold">
            SP
          </div>
          <div>
            <p class="text-sm font-medium">Sawan Parihar</p>
            <p class="text-xs text-slate-400">dotGenesis</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 flex flex-col relative overflow-hidden h-full">
      <header class="h-16 flex-shrink-0 glass border-b border-white/5 flex items-center justify-between px-6 md:hidden">
        <h1 class="text-xl font-bold text-gradient">dotG</h1>
        <!-- Mobile Menu Toggle (Mock) -->
        <button class="text-slate-300"><i data-feather="menu"></i></button>
      </header>
      
      <div class="flex-1 overflow-y-auto p-6 lg:p-10 relative z-10">
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </div>
      
      <!-- Decorative Background Elements -->
      <div class="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 rounded-full bg-indigo-500/10 blur-[100px] pointer-events-none"></div>
      <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 rounded-full bg-purple-500/10 blur-[100px] pointer-events-none"></div>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import feather from 'feather-icons';

onMounted(() => {
  feather.replace();
});
</script>

<style>
.nav-link {
  @apply flex items-center px-4 py-3 text-sm font-medium rounded-xl text-slate-400 hover:text-white hover:bg-white/5 transition-all duration-200;
}
.nav-link.active {
  @apply text-white bg-indigo-500/20 text-indigo-300;
  box-shadow: inset 2px 0 0 0 #818cf8;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
